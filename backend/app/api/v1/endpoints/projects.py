from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from app.models import models
from app.services import ai_service, pdf_service, email_service, database_service
import re
import os

# --- TODO: Implement proper authentication --- 
# from app.api.deps import get_current_creator # Dependency for protected routes

def get_current_creator_placeholder():
    # Placeholder: In a real app, this would validate a token and return creator data
    # For MVP, assume a fixed creator or bypass auth
    # creator = database_service.get_creator_by_email("test_creator@example.com")
    # if not creator:
    #     raise HTTPException(status_code=404, detail="Default creator not found")
    # return models.Creator(**creator) # Convert dict to Pydantic model
    print("WARNING: Authentication bypassed using placeholder.")
    return models.Creator(id=1, email="test_creator@example.com") # Dummy creator
# -------------------------------------------

router = APIRouter()

def run_project_generation_flow(request_data: models.ProjectRequest):
    """Background task to handle the full project generation and delivery."""
    print(f"--- Starting Project Generation for {request_data.requester_instagram_username} ---")

    # 1. Store initial request in DB
    # Ensure creator_id is passed correctly, potentially from the authenticated user
    request_entry = database_service.create_project_request_entry(request_data)
    if not request_entry or 'id' not in request_entry:
        print(f"Error: Failed to store project request for {request_data.requester_instagram_username}")
        return # Exit if saving request failed
    request_id = request_entry['id']
    print(f"Request {request_id} stored.")

    # 2. Generate Project Brief using AI
    brief_content = ai_service.generate_project_brief(request_data.comment_text)
    if "Error:" in brief_content:
        print(f"Error: AI generation failed for request {request_id}. Reason: {brief_content}")
        # TODO: Update status in DB to 'failed'
        return
    print(f"Request {request_id}: Brief generated.")

    # Extract title (simple approach: first line)
    title_match = re.search(r"Project Title: (.*)", brief_content)
    project_title = title_match.group(1).strip() if title_match else "Generated Project"

    # 3. Generate PDF
    pdf_filename = f"project_{request_data.requester_instagram_username}_{request_id}.pdf"
    pdf_path = pdf_service.generate_pdf_from_text(brief_content, pdf_filename)

    if not pdf_path:
        print(f"Error: PDF generation failed for request {request_id}.")
        # TODO: Update status in DB to 'failed'
        return
    print(f"Request {request_id}: PDF generated at {pdf_path}.")

    # 4. Save generated project details to DB (including PDF path/URL if uploaded)
    saved_project = database_service.save_generated_project(
        request_id=request_id,
        title=project_title,
        description=brief_content, # Save the full brief
        pdf_local_path=pdf_path # Pass path for potential upload
    )
    if not saved_project:
        print(f"Error: Failed to save generated project details for request {request_id}.")
        # Cleanup generated PDF?
        # os.remove(pdf_path)
        return
    print(f"Request {request_id}: Project details saved to DB.")

    # 5. Send Email (if email address is provided)
    if request_data.requester_email:
        email_subject = f"Your Custom Project Idea: {project_title}"
        email_body = f"""Hi {request_data.requester_instagram_username},<br><br>
        Here's the project brief generated based on your comment on the post: <a href='{request_data.instagram_post_url}'>{request_data.instagram_post_url}</a><br><br>
        Your comment: "{request_data.comment_text}"<br><br>
        Please find the project details attached.<br><br>
        Happy coding!<br>
        (Sent by AI Tutor Automation)
        """
        email_sent = email_service.send_email_with_attachment(
            to_email=request_data.requester_email,
            subject=email_subject,
            html_content=email_body,
            attachment_path=pdf_path
        )
        if email_sent:
            print(f"Request {request_id}: Email sent successfully to {request_data.requester_email}.")
            # TODO: Update status in DB to 'completed' or 'email_sent'
        else:
            print(f"Error: Failed to send email for request {request_id} to {request_data.requester_email}.")
            # TODO: Update status in DB to indicate email failure
    else:
        print(f"Request {request_id}: No email provided, skipping email step.")
        # TODO: Update status in DB to 'completed_no_email'

    # Optional: Clean up local PDF file after sending/saving (if not storing locally)
    # os.remove(pdf_path)

    print(f"--- Finished Project Generation for Request {request_id} ---")


@router.post("/generate-project", status_code=202) # 202 Accepted for background tasks
async def generate_project_endpoint(
    request: models.ProjectRequest,
    background_tasks: BackgroundTasks,
    # current_creator: models.Creator = Depends(get_current_creator_placeholder) # Use Depends for auth
):
    """API Endpoint to trigger project generation from a comment (Manual MVP)."""
    # Basic validation
    if not request.comment_text or not request.instagram_post_url or not request.requester_instagram_username:
        raise HTTPException(status_code=400, detail="Missing required fields: comment_text, instagram_post_url, requester_instagram_username")

    # --- Assign creator ID (Using placeholder/dummy ID for now) ---
    # In a real app, get this from the authenticated user (`current_creator.id`)
    request.creator_id = 1 # DUMMY ID
    # -----------------------------------------------------------

    # Validate email if provided
    # if request.requester_email: # Add more robust email validation if needed
    #     pass

    print(f"Received project generation request: {request.dict()}")

    # Add the generation process to background tasks
    background_tasks.add_task(run_project_generation_flow, request)

    return {"message": "Project generation started in the background. You will receive an email if provided."}

# Add other endpoints later (auth, progress tracking, dashboard data) 