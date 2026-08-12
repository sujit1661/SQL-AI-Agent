import os
import re
from groq import Client
from dotenv import load_dotenv

load_dotenv()

client = Client(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = (
    "You are a PostgreSQL SQL generator. "
    "You output ONLY raw PostgreSQL SELECT statements — nothing else. "
    "No explanations. No markdown. No backticks. No commentary. "
    "If the request cannot be answered from the schema, output exactly: NOT_POSSIBLE"
)


def generate_sql(question: str, schema_text: str) -> str:
    user_prompt = f"""Schema:
{schema_text}

Question: {question}

Rules:
- Output a single valid PostgreSQL SELECT query.
- Use only tables and columns that exist in the schema above.
- Never invent table or column names.
- Use ILIKE for case-insensitive text searches.
- Use JOINs when needed with valid foreign key relationships.
- For greetings, off-topic, or impossible requests: output exactly "NOT_POSSIBLE"
- Output ONLY the SQL query — no markdown, no explanation, no backticks, no comments."""

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": user_prompt},
            ],
            temperature=0.0,
            max_tokens=512,
            stream=False,
        )

        raw = completion.choices[0].message.content or ""
        raw = raw.strip()

        # Handle thinking tags
        if "</think>" in raw:
            raw = raw.split("</think>")[-1].strip()

        # Strip markdown code fences
        raw = re.sub(r"```(?:sql)?", "", raw, flags=re.IGNORECASE)
        raw = raw.replace("```", "").strip()

        # Check for NOT_POSSIBLE
        if raw.upper() == "NOT_POSSIBLE":
            return "NOT_POSSIBLE"

        # Extract SELECT statement (handles if there's prose around it)
        match = re.search(r"(SELECT\b.+?)(?:;|$)", raw, re.IGNORECASE | re.DOTALL)
        if match:
            sql = match.group(1).strip()
            if not sql.endswith(";"):
                sql += ";"
            return sql

        # No valid SQL found
        return "NOT_POSSIBLE"

    except Exception as e:
        print(f"LLM Error: {e}")
        return "NOT_POSSIBLE"
