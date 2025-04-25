from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
from app.core.config import settings
import base64
import os

def send_email_with_attachment(to_email: str, subject: str, html_content: str, attachment_path: str) -> bool:
    """Sends an email with a PDF attachment using SendGrid."""
    if not settings.SENDGRID_API_KEY:
        print("Error: SendGrid API Key not configured.")
        return False
    if not os.path.exists(attachment_path):
        print(f"Error: Attachment file not found: {attachment_path}")
        return False

    message = Mail(
        from_email=settings.EMAIL_FROM,
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )

    # Read attachment file and encode it
    try:
        with open(attachment_path, 'rb') as f:
            data = f.read()
        encoded_file = base64.b64encode(data).decode()
    except Exception as e:
        print(f"Error reading attachment file: {e}")
        return False

    attached_file = Attachment(
        FileContent(encoded_file),
        FileName(os.path.basename(attachment_path)),
        FileType('application/pdf'),
        Disposition('attachment')
    )
    message.attachment = attached_file

    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"[Email Service] Email sent to {to_email}. Status code: {response.status_code}")
        # Consider status codes other than 2xx as potential failures
        return 200 <= response.status_code < 300
    except Exception as e:
        print(f"Error sending email via SendGrid: {e}")
        return False 