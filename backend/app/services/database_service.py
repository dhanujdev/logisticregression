from supabase import create_client, Client
from app.core.config import settings
from app.models import models # Import your Pydantic models
from typing import Optional, List, Dict, Any
import datetime

# Initialize Supabase client
supabase: Client | None = None
if settings.SUPABASE_URL and settings.SUPABASE_KEY:
    try:
        supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        print("[DB Service] Supabase client initialized.")
    except Exception as e:
        print(f"Error initializing Supabase client: {e}")
else:
    print("[DB Service] Supabase URL or Key not configured. Database operations will fail.")

# --- Placeholder functions for Database interactions ---
# Replace these with actual Supabase calls based on your table structure

def get_creator_by_email(email: str) -> Optional[Dict[str, Any]]:
    """Placeholder: Fetches a creator by email."""
    if not supabase: return None
    try:
        response = supabase.table('creators').select("*").eq('email', email).limit(1).execute()
        if response.data:
            return response.data[0]
        return None
    except Exception as e:
        print(f"Error fetching creator by email '{email}': {e}")
        return None

def create_project_request_entry(request_data: models.ProjectRequest) -> Optional[Dict[str, Any]]:
    """Placeholder: Stores the initial project request."""
    if not supabase: return None
    try:
        # Note: Supabase client typically uses snake_case keys
        data_to_insert = {
            "creator_id": request_data.creator_id,
            "instagram_post_url": str(request_data.instagram_post_url),
            "comment_text": request_data.comment_text,
            "requester_instagram_username": request_data.requester_instagram_username,
            "requester_email": request_data.requester_email,
            # Add other fields like status, timestamps if needed
        }
        response = supabase.table('project_requests').insert(data_to_insert).execute()
        if response.data:
            return response.data[0]
        return None
    except Exception as e:
        print(f"Error creating project request entry: {e}")
        return None

def save_generated_project(request_id: int, title: str, description: str, pdf_local_path: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Placeholder: Saves the generated project details."""
    if not supabase: return None
    try:
        # Optional: Upload PDF to Supabase Storage and get URL
        pdf_storage_url = None
        if pdf_local_path:
            # pdf_storage_url = upload_pdf_to_storage(pdf_local_path)
            pass # Implement upload logic here if needed

        data_to_insert = {
            "request_id": request_id,
            "project_title": title,
            "project_description": description, # Store the raw generated text
            "pdf_url": pdf_storage_url, # URL from storage or null
            "created_at": datetime.datetime.now().isoformat() # Supabase often handles timestamps
        }
        response = supabase.table('generated_projects').insert(data_to_insert).execute()
        if response.data:
            return response.data[0]
        return None
    except Exception as e:
        print(f"Error saving generated project: {e}")
        return None

# Add other functions as needed (e.g., track_progress, get_user_progress, etc.)

# Example: Function to upload file to Supabase Storage (Implement if needed)
# def upload_pdf_to_storage(local_path: str) -> Optional[str]:
#     if not supabase: return None
#     try:
#         bucket_name = "project_pdfs"
#         destination_path = f"generated/{os.path.basename(local_path)}"
#         with open(local_path, 'rb') as f:
#             # Check if bucket exists, create if not (handle permissions appropriately)
#             # ... check/create bucket logic ...
#             supabase.storage.from_(bucket_name).upload(destination_path, f)
#         # Construct the public URL (adjust based on your bucket settings)
#         public_url = supabase.storage.from_(bucket_name).get_public_url(destination_path)
#         print(f"[DB Service] Uploaded {local_path} to Supabase Storage: {public_url}")
#         return public_url
#     except Exception as e:
#         print(f"Error uploading PDF to Supabase Storage: {e}")
#         return None 