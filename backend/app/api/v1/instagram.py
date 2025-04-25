from fastapi import APIRouter, Header, HTTPException, Depends
from typing import Dict
from app.core.config import settings
from app.services.ai_service import generate_project
from app.services.pdf_service import create_pdf
from app.services.email_service import send_email

router = APIRouter()

@router.post("/webhook")
async def instagram_webhook(
    payload: Dict,
    x_hub_signature: str = Header(...)
):
    # Verify webhook signature
    if not verify_signature(payload, x_hub_signature):
        raise HTTPException(status_code=400, detail="Invalid signature")
    
    # Process webhook event
    entry = payload.get("entry", [{}])[0]
    changes = entry.get("changes", [{}])[0]
    
    if changes["field"] == "comments":
        # Process comment for project generation
        await process_comment(changes["value"])
    elif changes["field"] == "likes":
        # Update learner progress
        await update_progress(changes["value"])
    
    return {"status": "ok"}

@router.get("/auth")
async def instagram_auth(code: str):
    # Handle Instagram OAuth
    try:
        # Exchange code for access token
        token_data = await exchange_code_for_token(code)
        
        # Store creator credentials
        await store_creator_credentials(token_data)
        
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def process_comment(comment_data: Dict):
    # Extract relevant information
    user_id = comment_data["from"]["id"]
    comment_text = comment_data["text"]
    
    # Generate project using AI
    project = await generate_project(comment_text)
    
    # Create PDF
    pdf_url = await create_pdf(project)
    
    # Send email
    await send_email(user_id, pdf_url)
    
    return project

async def update_progress(like_data: Dict):
    # Update learner progress based on like
    user_id = like_data["from"]["id"]
    content_id = like_data["content_id"]
    
    # Update progress in database
    await update_learner_progress(user_id, content_id)
    
    return {"status": "updated"} 