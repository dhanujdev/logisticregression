import pdfkit
from app.core.config import settings
import os
from typing import Optional

# Configure pdfkit (optional, if wkhtmltopdf is not in system PATH)
config = None
if settings.PDFKIT_CONFIG and os.path.exists(settings.PDFKIT_CONFIG):
    config = pdfkit.configuration(wkhtmltopdf=settings.PDFKIT_CONFIG)

def generate_pdf_from_text(content: str, output_filename: str) -> Optional[str]:
    """Generates a PDF file from text content and saves it.

    Args:
        content: The text content (can be HTML formatted for better results).
        output_filename: The desired name for the output PDF file (without path).

    Returns:
        The full path to the generated PDF file, or None if generation failed.
    """
    output_dir = "generated_projects" # Store generated PDFs here
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, output_filename)

    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'no-outline': None
    }

    try:
        # Use HTML input for better formatting potential
        html_content = f"""<!DOCTYPE html>
        <html>
        <head><meta charset="utf-8"></head>
        <body><pre>{content}</pre></body>
        </html>"""
        # pdfkit.from_string(content, output_path, options=options, configuration=config)
        # Using from_string with HTML for potentially better formatting
        pdfkit.from_string(html_content, output_path, options=options, configuration=config)

        print(f"[PDF Service] PDF generated successfully: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error generating PDF: {e}")
        # Consider more robust error handling
        # Check if wkhtmltopdf is installed and accessible
        if isinstance(e, OSError) and 'No wkhtmltopdf executable found' in str(e):
            print("ERROR: wkhtmltopdf command not found.")
            print("Please install wkhtmltopdf: https://wkhtmltopdf.org/downloads.html")
            print("If installed but not in PATH, set PDFKIT_CONFIG in your .env file.")
        return None 