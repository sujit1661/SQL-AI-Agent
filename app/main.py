from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware  # <--- 1. IMPORT THIS
from sqlmodel import Session, text

from db import get_session
from schema import get_db_schema, format_schema_for_llm
from llm import generate_sql

app = FastAPI()

# <--- 2. ADD THIS BLOCK --->
# This allows your frontend (running in the browser) to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all connections (Safety for local dev)
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, etc.
    allow_headers=["*"],  # Allows all headers
)



@app.get("/")
def health():
    return {"status": "alive"}


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
        return "error"
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