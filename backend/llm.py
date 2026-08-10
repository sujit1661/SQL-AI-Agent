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
- Use JOINs only when a valid foreign key relationship exists.
- For greetings, unrelated questions, or impossible requests output: NOT_POSSIBLE
- Output the raw SQL only — no markdown, no explanation, no backticks."""

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

        # Strip thinking tags (some models emit <think>...</think>)
        if "</think>" in raw:
            raw = raw.split("</think>")[-1]

        # Strip markdown code fences
        raw = re.sub(r"```(?:sql)?", "", raw, flags=re.IGNORECASE)
        raw = raw.replace("```", "").strip()

        # If the model snuck in an explanation before the SQL, extract the first SELECT
        if raw.upper().startswith("NOT_POSSIBLE"):
            return "NOT_POSSIBLE"

        # Pull out the first SELECT … ; block if surrounded by prose
        match = re.search(r"(SELECT\b.*?)(?:;|$)", raw, re.IGNORECASE | re.DOTALL)
        if match:
            sql = match.group(1).strip()
            # Add back trailing semicolon if it was captured
            if raw.rstrip().endswith(";"):
                sql += ";"
            return sql

        # If nothing looks like SQL at all, give up
        return "NOT_POSSIBLE"

    except Exception as e:
        print(f"LLM Error: {e}")
        return "NOT_POSSIBLE"
