# Backend API (FastAPI)

This directory contains the Python FastAPI backend for the AI Tutor Automation platform.

## Setup and Running

1.  Navigate to the `backend` directory: `cd backend`
2.  Create a virtual environment: `python -m venv venv`
3.  Activate the virtual environment:
    *   macOS/Linux: `source venv/bin/activate`
    *   Windows: `.\venv\Scripts\activate`
4.  Install dependencies: `pip install -r requirements.txt`
5.  **Important:** Create a `.env` file by copying `.env.example` (`cp .env.example .env`) and fill in your actual API keys and database credentials.
6.  Run the development server: `uvicorn main:app --reload --port 8000`

The API documentation (Swagger UI) will be available at `http://localhost:8000/docs`.

## Structure

-   `main.py`: FastAPI application entry point.
-   `requirements.txt`: Python package dependencies.
-   `.env.example`: Template for environment variables.
-   `app/`: Main application code.
    -   `api/`: API route definitions.
    -   `core/`: Core logic (AI integration, PDF generation, config).
    -   `models/`: Data models (Pydantic schemas, potentially ORM models).
    -   `services/`: Business logic implementation.
    -   `utils/`: Utility functions. 