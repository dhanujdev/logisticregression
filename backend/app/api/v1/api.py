from fastapi import APIRouter
from app.api.v1.endpoints import projects # Import other endpoint routers here

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(projects.router, prefix="/projects", tags=["Projects"])
# api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"]) # Example
# api_router.include_router(progress.router, prefix="/progress", tags=["Progress Tracking"]) # Example 