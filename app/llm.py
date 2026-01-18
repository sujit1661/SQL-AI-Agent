import os
from groq import Client
from dotenv import load_dotenv

load_dotenv()

client = Client(api_key=os.getenv("GROQ_API_KEY"))


def generate_sql(question: str, schema_text: str) -> str:
    prompt = f"""
    You are a PostgreSQL Expert. 

    Database Schema:
    {schema_text}

    User Question: {question}

    Rules:
    1. Return valid PostgreSQL SQL ONLY.
    2. If the user asks for "all data" or "everything", select all columns from the table.
    3. Do NOT use markdown (no ```sql).
    4. Do NOT explain.
    5. If the request is impossible, return: NOT_POSSIBLE
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # Reliable model for SQL
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            max_tokens=400,
            stream=False
        )

        sql = completion.choices[0].message.content

        # Clean up any markdown or thinking tags
        if "</think>" in sql:
            sql = sql.split("</think>")[-1]

        return sql.replace("```sql", "").replace("```", "").strip()

    except Exception as e:
        print(f"LLM Error: {e}")
        return "NOT_POSSIBLE"