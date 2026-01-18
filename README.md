# AI-Based-SQL-Agent

Natural language–driven SQL query engine built with FastAPI, enabling safe database querying without writing SQL.

## 🧠 Overview

AI-Based-SQL-Agent allows users to interact with a relational database using **plain English** instead of SQL.  
Users can submit natural language questions, and the system generates **schema-aware, SELECT-only SQL queries**, executes them, and returns the results.

This project is designed to simplify database access and reduce the complexity of writing SQL, especially for **complex joins and nested queries**.

## 💡 Motivation

While working with databases, writing and maintaining complex SQL queries—especially involving joins and conditions—was time-consuming and error-prone.  
This project was built to eliminate that friction by providing a **natural language interface** for database querying.

## 🚀 Features

- Natural language to SQL conversion  
- No SQL knowledge required  
- Generates **SELECT-only** queries for safety  
- Schema-aware query generation  
- FastAPI-based REST API  
- Handles unsupported queries gracefully  

## 🛠 Tech Stack

- Python  
- FastAPI  
- PostgreSQL  
- LLM-based query generation  
- Uvicorn  


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
