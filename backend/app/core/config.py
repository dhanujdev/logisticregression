import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Tutor Automation"
    API_V1_STR: str = "/api/v1"

    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")

    # LLM Provider (e.g., OpenAI)
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    # Or for Gemini: GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")

    # Email Provider (e.g., SendGrid)
    SENDGRID_API_KEY: str = os.getenv("SENDGRID_API_KEY", "")
    EMAIL_FROM: str = os.getenv("EMAIL_FROM", "noreply@example.com") # Default sender

    # PDF Generation Tool (e.g., path if using local wkhtmltopdf with pdfkit)
    PDFKIT_CONFIG: str | None = os.getenv("PDFKIT_CONFIG") # Optional path to wkhtmltopdf

    # Celery / Background Tasks
    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

    class Config:
        case_sensitive = True
        # Allows loading from .env file via load_dotenv()
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings() 