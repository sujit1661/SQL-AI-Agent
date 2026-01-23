# AI-Based SQL Agent 🤖🗄️

A **Natural Language–driven SQL query engine** built with **FastAPI** that allows users to query databases safely **without writing SQL**.

---

## 🧠 Overview

**AI-Based SQL Agent** enables users to interact with a relational database using **plain English**.  
Instead of manually writing SQL queries, users can ask questions like:

> *“Show all users who signed up last month”*

The system automatically:
- Converts natural language into **schema-aware SQL**
- Ensures **SELECT-only queries** for safety
- Executes the query
- Returns the result

This project is ideal for simplifying database access and handling **complex joins or filters** without SQL expertise.

---

## 💡 Motivation

Writing and maintaining complex SQL queries—especially with joins, filters, and nested conditions—can be:
- Time-consuming  
- Error-prone  
- Hard to maintain  

This project was built to remove that friction by introducing a **safe natural language interface** for database querying using an LLM.

---

## 🚀 Features

✅ Natural language → SQL conversion  
✅ No SQL knowledge required  
✅ **SELECT-only query enforcement** (safe by design)  
✅ Schema-aware query generation  
✅ FastAPI-powered REST API  
✅ Graceful handling of unsupported queries  
✅ Simple frontend for testing queries  

---

## 📁 Project Structure

```
AI-Based-SQL-Agent/
│
├── app/
│   ├── __init__.py
│   ├── db.py              # Database connection logic
│   ├── llm.py             # LLM-based SQL generation
│   ├── schema.py          # Database schema definitions
│   ├── main.py            # FastAPI application
│   └── index.html         # Simple frontend UI
│
├── .env                   # Environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

- **Python**
- **FastAPI**
- **PostgreSQL**
- **LLM (Groq / similar)**
- **Uvicorn**
- HTML (basic frontend)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```
git clone https://github.com/sujit1661/AI-Based-SQL-Agent.git
cd AI-Based-SQL-Agent
```

---

### 2️⃣ Create & Activate Virtual Environment
```
python -m venv venv
```

**Activate it:**

**Windows**
```
venv\Scripts\activate
```

**Linux / macOS**
```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file and add:

```
DATABASE_URL=your_postgres_connection_string
GROQ_API_KEY=your_groq_api_key
```

---

### 5️⃣ Run the Application
```
uvicorn app.main:app --reload
```

Server will start at:
```
http://127.0.0.1:8000
```

---

### 6️⃣ Open the Frontend

Open `index.html` in your browser  
Start querying the database using **natural language**.

---

## 📌 Example Queries

- “Show all users”
- “List orders placed in the last 7 days”
- “Get total sales grouped by category”

---

## 🔒 Safety Design

- Only **SELECT queries** are generated  
- INSERT, UPDATE, DELETE, DROP are blocked  
- Queries validated against schema  

---

## 🚀 Future Enhancements

- Authentication & user sessions
- Query history
- Visualization of results
- Support for multiple databases
- Role-based access control

---

## 👤 Author

**Sujit**  
Aspiring Backend / AI Engineer 🚀

---

⭐ If you find this project useful, please give it a star on GitHub!
