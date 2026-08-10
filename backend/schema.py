from sqlalchemy import inspect
from typing import Dict, List
from db import engine


def get_db_schema() -> Dict[str, List[str]]:
    """
    Connects to DB and gets actual table/column names.
    """
    schema_map = {}
    try:
        inspector = inspect(engine)
        # 1. Get all table names in public schema
        tables = inspector.get_table_names(schema="public")

        for table in tables:
            # 2. Get columns for each table
            columns = inspector.get_columns(table, schema="public")
            # Format: "name (type)"
            col_strings = [f"{col['name']} ({col['type']})" for col in columns]
            schema_map[table] = col_strings

    except Exception as e:
        print(f"Schema Error: {e}")

    return schema_map


def format_schema_for_llm(schema: Dict[str, List[str]]) -> str:
    lines = []
    for table, cols in schema.items():
        lines.append(f"Table: {table}")
        lines.append(f"Columns: {', '.join(cols)}")
        lines.append("")  # Empty line separator
    return "\n".join(lines)