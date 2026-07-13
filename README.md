# 🤖 AI-Based SQL Agent

> A Natural Language to SQL engine built with **FastAPI** that allows users to query databases using plain English—without writing SQL.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?logo=postgresql)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

AI-Based SQL Agent enables users to interact with a relational database using **natural language**.

Instead of writing SQL queries manually, users can simply ask questions such as:

> **"Show all users who signed up last month."**

The application automatically:

- Converts natural language into SQL
- Understands the database schema
- Generates safe **SELECT-only** queries
- Executes the query
- Returns the results instantly

This makes database interaction faster, safer, and more accessible for users who are not familiar with SQL.

---

## ✨ Features

- 🔹 Natural Language → SQL conversion
- 🔹 Schema-aware SQL generation
- 🔹 Secure **SELECT-only** query execution
- 🔹 FastAPI REST API
- 🔹 PostgreSQL integration
- 🔹 Graceful handling of unsupported queries
- 🔹 Simple HTML frontend for testing
- 🔹 Easy to configure and extend

---

## 🏗️ Project Structure

```text
AI-Based-SQL-Agent/
│
├── app/
│   ├── __init__.py
│   ├── db.py              # Database connection
│   ├── llm.py             # LLM prompt & SQL generation
│   ├── schema.py          # Database schema
│   ├── main.py            # FastAPI application
│   └── index.html         # Frontend
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| FastAPI | REST API |
| PostgreSQL | Database |
| Groq API / LLM | Natural Language to SQL |
| Uvicorn | ASGI Server |
| HTML | Simple Frontend |

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/sujit1661/AI-Based-SQL-Agent.git
cd AI-Based-SQL-Agent
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=your_postgresql_connection_string
GROQ_API_KEY=your_groq_api_key
```

---

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

Server will be available at:

```
http://127.0.0.1:8000
```

---

### 6. Open the Frontend

Open the `index.html` file in your browser and start querying your database using natural language.

---

## 💬 Example Queries

Try asking questions like:

- Show all users
- Display all employees from the HR department
- List orders placed in the last 7 days
- Show products with price greater than 1000
- Get total sales grouped by category
- Find customers from Pune

---

## 🔒 Safety

This project is designed with safety in mind.

- ✅ Only **SELECT** statements are allowed
- ✅ INSERT, UPDATE, DELETE, DROP, ALTER, and TRUNCATE are blocked
- ✅ Queries are validated before execution
- ✅ Schema-aware SQL generation minimizes invalid queries

---

## 🚀 Future Improvements

- User Authentication
- Query History
- Result Visualization
- Multi-Database Support
- Role-Based Access Control (RBAC)
- Conversation Memory
- Query Optimization

---

## 👨‍💻 Author

**Sujit Sadalage**

Aspiring **AI Engineer | Backend Developer | Python Developer**

- GitHub: https://github.com/sujit1661

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future improvements.

---

## 📄 License

This project is intended for learning and educational purposes. Feel free to fork, modify, and build upon it.
