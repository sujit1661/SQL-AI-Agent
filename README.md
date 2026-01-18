🤖 AI-Based SQL Agent
A natural language–driven SQL query engine built with FastAPI, enabling safe database querying without writing SQL.


🧠 Overview
AI-Based SQL Agent allows users to interact with a relational database using plain English instead of SQL.
Users submit natural language questions, and the system:

Converts them into schema-aware SQL queries

Ensures queries are SELECT-only for safety

Executes the queries and returns results

This project is designed to simplify database access and eliminate the need to write complex joins or nested SQL queries.



💡 Motivation

Writing and maintaining complex SQL queries—especially those involving multiple joins and conditions—can be time-consuming and error-prone.

This project was built to:

Reduce SQL complexity

Improve productivity

Provide a safe, AI-powered natural language interface to databases



🚀 Features

🔤 Natural Language → SQL conversion

🛡️ SELECT-only query generation (safe by design)

🧠 Schema-aware SQL generation

⚡ FastAPI-based REST API

🗄️ PostgreSQL database support

❌ Graceful handling of unsupported or unsafe queries



🛠 Tech Stack

Python

FastAPI

PostgreSQL

LLM-based query generation

Uvicorn


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/sujit1661/AI-Based-SQL-Agent.git
cd AI-Based-SQL-Agent


2️⃣ Create & Activate Virtual Environment
python -m venv venv
Activate it:

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate


3️⃣ Install Dependencies
pip install -r requirements.txt


4️⃣ Configure Environment Variables

Add the following:

Database URL

Groq API Key

(Use .env or environment variables as per your setup)


5️⃣ Run the Application
uvicorn main:app --reload


6️⃣ Open the Frontend

Open index.html in your browser

Start querying the database using natural language
