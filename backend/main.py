from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import API routers (will be created later)
from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS (Cross-Origin Resource Sharing)
# Set origins to the frontend URL in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for development
    # allow_origins=["http://localhost:3000", "YOUR_FRONTEND_URL"], # Production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": f"Welcome to {settings.PROJECT_NAME}"}

# Include the API router (uncomment when ready)
app.include_router(api_router, prefix=settings.API_V1_STR)

# Placeholder for other app setup (e.g., database connection, background tasks) 