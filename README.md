# Portfolio Project - Adolfo Nicolas Vargas

This is a dynamic, premium portfolio built with React (Vite) for the frontend, and a Flask (Python) backend utilizing SQLite for project data management. It showcases my personal projects and acts as an interactive digital resume.

## Tech Stack
- **Frontend**: React, Vite, Lucide-React, custom CSS (Modern Glassmorphism UI)
- **Backend**: Python, Flask, Flask-CORS, SQLite

## Setup Instructions

### Backend setup
1. Open terminal in the root directory.
2. Create a virtual environment: `python -m venv backend/venv`
3. Activate the virtual environment and install dependencies:
   `backend\venv\Scripts\pip install flask flask-cors`
4. Initialize the database: `python backend/setup_db.py`
5. Start the server: `python backend/app.py`

### Frontend setup
1. Navigate to the `frontend` directory: `cd frontend`
2. Install dependencies: `npm install`
3. Start the Vite development server: `npm run dev`

## Features
- Dynamic API data fetching with Flask.
- Responsive, animated UI with a dynamic interactive project modal.
- Built-in category filtering.
