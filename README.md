# Logistic Regression Project

This project consists of a Python backend and a Next.js frontend for logistic regression modeling.

## Project Structure

- `backend/`: Python backend with FastAPI
  - Contains the logistic regression model implementation
  - API endpoints for data processing and model training
  
- `frontend/`: Next.js frontend application
  - User interface for data visualization and model interaction
  - Dashboard for results

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```
   python main.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Run the development server:
   ```
   npm run dev
   ```

## Usage

Access the application at `http://localhost:3000` once both backend and frontend servers are running. 