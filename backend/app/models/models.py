from pydantic import BaseModel, EmailStr, HttpUrl
from typing import Optional
import datetime

# Base models
class CreatorBase(BaseModel):
    email: EmailStr
    instagram_username: Optional[str] = None

class CreatorCreate(CreatorBase):
    password: str # In a real app, hash this securely

class Creator(CreatorBase):
    id: int # Or UUID
    # Add other fields like name, etc.
    class Config:
        from_attributes = True # orm_mode = True

# --- Authentication --- (Very basic placeholders)
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# --- Course/Progress Tracking --- (Placeholders for now)
class CourseModule(BaseModel):
    id: int
    title: str
    post_url: HttpUrl

class UserProgress(BaseModel):
    user_instagram_id: str
    completed_modules: list[int] = [] # List of module IDs

# --- Project Generation --- (Core MVP feature)
class ProjectRequest(BaseModel):
    creator_id: int # Link to the creator
    instagram_post_url: HttpUrl
    comment_text: str
    requester_instagram_username: str
    requester_email: Optional[EmailStr] = None # May need separate opt-in

class ProjectGenerateInput(BaseModel):
    comment_text: str
    # Could add context like course topic, creator style, etc.

class GeneratedProject(BaseModel):
    id: int
    request_id: int # Link back to ProjectRequest
    project_title: str
    project_description: str # Generated content
    pdf_url: Optional[str] = None # URL if stored (e.g., Supabase storage)
    created_at: datetime.datetime

    class Config:
        from_attributes = True 