import os
from pathlib import Path

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, text

from db import get_session
from schema import get_db_schema, format_schema_for_llm
from llm import generate_sql

# Resolve the frontend directory relative to this file
FRONTEND_DIR = Path(__file__).parent.parent / "frontend"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve all files inside frontend/ as static assets (CSS, JS, images, etc.)
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


@app.get("/", include_in_schema=False)
def root():
    """Serve the landing page at the root URL."""
    return FileResponse(str(FRONTEND_DIR / "landing.html"))


@app.get("/app", include_in_schema=False)
def studio():
    """Serve the main SQL Studio app."""
    return FileResponse(str(FRONTEND_DIR / "index.html"))


@app.get("/profile", include_in_schema=False)
def profile():
    """Serve the owner profile page."""
    return FileResponse(str(FRONTEND_DIR / "profile.html"))


@app.get("/schema")
def check_schema():
    """Returns the database schema so the frontend sidebar can list tables."""
    return get_db_schema()


@app.post("/generate")
def generate_and_execute(question: str, session: Session = Depends(get_session)):
    # 1. Get Fresh Schema
    raw_schema = get_db_schema()
    # 2. Format for LLM
    schema_str = format_schema_for_llm(raw_schema)
    # 3. Generate SQL
    sql_query = generate_sql(question, schema_str)

    if sql_query == "NOT_POSSIBLE":
        return {
            "question": question,
            "sql": None,
            "results": [],
            "message": "I couldn't generate a SQL query for that. Try asking something about your data — for example, 'Show me all users' or 'Count orders by status'."
        }
    try:
        # Safety check: Prevent destructive queries (basic)
        if not sql_query.strip().lower().startswith("select"):
            return {
                "question": question,
                "sql": sql_query,
                "error": "For safety, only SELECT queries are allowed."
            }

        result = session.exec(text(sql_query))

        # 5. Convert rows to list of dicts
        keys = result.keys()
        data = [dict(zip(keys, row)) for row in result.all()]

        return {
            "question": question,
            "sql": sql_query,
            "results": data
        }
    except Exception as e:
        return {
            "question": question,
            "sql": sql_query,
            "error": str(e)
        }