# SQL Studio AI

A natural language interface for PostgreSQL powered by Groq and llama-3.1. Ask questions about your database in plain English and get instant SQL-generated results.

## Features

- **Natural Language → SQL**: Ask questions in plain English, get SQL queries automatically generated
- **Schema-aware**: LLM receives live database schema to generate valid, accurate SQL
- **Read-safe**: Only SELECT queries execute — no destructive operations
- **Fast**: ~200ms average query time via Groq inference
- **Instant results**: Full-stack FastAPI + React interface with live schema explorer
- **CSV export**: Download results directly from the UI
- **Docker ready**: One-command deployment with docker-compose

## Tech Stack

- **Backend**: FastAPI, PostgreSQL, SQLModel, Groq LLM
- **Frontend**: React 18, pure CSS (no framework)
- **LLM**: llama-3.1-8b-instant on Groq
- **Deployment**: Docker & docker-compose ready

## Quick Start

### Local Development

1. **Install Python dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Set up PostgreSQL** (or use Docker for database):
   ```bash
   # Option 1: Local PostgreSQL
   # Update DATABASE_URL in .env with your connection string
   
   # Option 2: Docker for DB only
   docker run -d \
     --name postgres-sql-studio \
     -e POSTGRES_DB=postgres \
     -e POSTGRES_USER= \
     -e POSTGRES_PASSWORD= \
     -p 5432:5432 \
     postgres:16-alpine
   ```

3. **Set environment variables** (already in `.env`):
   ```
   DATABASE_URL=
   GROQ_API_KEY=
   ```

4. **Run the backend**:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

5. **Open in browser**:
   - Landing page: `http://localhost:8000`
   - App: `http://localhost:8000/app`
   - Profile: `http://localhost:8000/profile`

### Docker Compose (Recommended for Production)

1. **Ensure `.env` is configured** with your Groq API key:
   ```env
   GROQ_API_KEY=
   DB_NAME=
   DB_USER=
   DB_PASSWORD=
   ```

2. **Build and start**:
   ```bash
   docker-compose up --build
   ```

3. **Access the app**:
   - App: `http://localhost:8000`
   - Database is automatically provisioned on postgres service

4. **Stop**:
   ```bash
   docker-compose down
   # To also remove the database volume:
   docker-compose down -v
   ```

## Directory Structure

```
SQL Agent/
├── backend/
│   ├── main.py           # FastAPI app with routes
│   ├── db.py             # Database connection setup
│   ├── schema.py         # Schema introspection
│   ├── llm.py            # LLM integration with Groq
│   └── __init__.py
├── frontend/
│   ├── landing.html      # Public landing page
│   ├── index.html        # Main SQL Studio app interface
│   └── profile.html      # Owner profile (Sujit Sadalage)
├── Dockerfile            # Multi-stage Docker build
├── docker-compose.yml    # Full stack setup
├── .dockerignore         # Docker build optimization
├── requirements.txt      # Python dependencies
├── .env                  # Environment configuration
└── README.md             # This file
```

## API Endpoints

- `GET /` — Landing page
- `GET /app` — SQL Studio interface
- `GET /profile` — Owner profile
- `GET /schema` — Returns live database schema
- `POST /generate` — Generates and executes SQL query
  - **Params**: `question` (string)
  - **Response**: `{ question, sql, results[], message?, error? }`

## Environment Variables

```env
# Database (local development — localhost)
DATABASE_URL=

# Groq API Key (required)
GROQ_API_KEY=your_groq_api_key

# Docker environment (used in docker-compose)
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=
```

**Note**: When running in Docker, the `DATABASE_URL` is automatically overridden to use the `db` service name for networking: ``

## Example Queries

Try asking questions like:

- "Show me all users"
- "How many orders were placed last month?"
- "What are the top 10 products by revenue?"
- "List customers from New York"
- "Find employees in the HR department"
- "Show total sales grouped by category"

## Safety & Security

- ✅ **SELECT-only enforcement**: Only `SELECT` queries execute — `DELETE`, `UPDATE`, `DROP`, `ALTER`, `TRUNCATE` are blocked
- ✅ **Schema-aware generation**: LLM receives live schema to minimize hallucinated column names
- ✅ **Input validation**: All inputs are sanitized before execution
- ✅ **Proper error handling**: Invalid queries return friendly error messages

## Performance

- **Query generation**: ~200ms via Groq (llama-3.1-8b-instant)
- **Database query**: Depends on query complexity and dataset size
- **Total round-trip**: Usually under 500ms for typical queries

## Troubleshooting

### Docker Issues

**Build fails with "requirements.txt not found"**
- Ensure you're in the project root directory when running `docker-compose`
- Check that `Dockerfile` has the correct path to `requirements.txt`

**Container can't connect to database**
- Wait a few seconds for PostgreSQL to initialize (health checks handle this)
- Check logs: `docker-compose logs`

**API returns connection error**
- Ensure `docker-compose.yml` `depends_on` is set correctly
- Check `DATABASE_URL` in `.env` uses `db` service name (not `localhost`)

### Local Development Issues

**"Module not found" errors**
- Activate virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
- Install dependencies: `pip install -r requirements.txt`

**Database connection refused**
- Check PostgreSQL is running on the configured host/port
- Verify `DATABASE_URL` in `.env` is correct

### Groq API Issues

**"Invalid API key"**
- Check `GROQ_API_KEY` in `.env` is correct
- Verify key has not expired or been revoked

**Rate limiting errors**
- Groq has rate limits on free tier — wait before retrying
- Consider upgrading or caching frequent queries

## Deployment to Production

### Cloud Deployment (Docker)

1. **Push image to registry**:
   ```bash
   docker build -t your-registry/sql-studio:latest .
   docker push your-registry/sql-studio:latest
   ```

2. **Set secure environment variables** in your cloud platform
3. **Deploy with docker-compose** or orchestration (Kubernetes, etc.)

### Security Checklist

- [ ] Rotate database password
- [ ] Use environment-specific Groq API keys
- [ ] Enable HTTPS/SSL
- [ ] Add authentication/authorization layer
- [ ] Set up database backups
- [ ] Monitor query logs for suspicious activity
- [ ] Rate limit API endpoints
- [ ] Add CORS restrictions

## Architecture

```
┌─────────────────────────────────────────────┐
│           React Frontend (Landing)          │
│         SQL Studio Chat Interface            │
│           Owner Profile Page                │
└────────────────┬────────────────────────────┘
                 │
                 │ HTTP/REST
                 ▼
        ┌────────────────────┐
        │   FastAPI Backend   │
        │  - Route handlers   │
        │  - Query generation │
        │  - Result formatting│
        └────────┬───────────┘
                 │
      ┌──────────┴──────────┐
      │                     │
      ▼                     ▼
  PostgreSQL            Groq API
  (Data Store)      (LLM Inference)
```

## Features in Detail

### Landing Page
- Hero section with animated diagonal line
- "How it works" pipeline (3-step process)
- Capabilities grid
- Tech stack marquee
- Call-to-action buttons
- Responsive mobile design

### SQL Studio App
- Sidebar with live schema explorer
- Chat-like message interface
- SQL generation display
- Results table with pagination
- CSV export functionality
- Connection status indicator
- Mobile hamburger navigation

### Profile Page
- Owner introduction (Sujit Sadalage)
- Animated avatar with gradient border
- Project statistics
- Inspirational quote in Instrument Serif
- Project details with tech stack
- Links to app and contact

## Future Enhancements

- [ ] Multi-database support (MySQL, SQLite, etc.)
- [ ] Query history & bookmarks
- [ ] User authentication & authorization
- [ ] Advanced visualization (charts, graphs)
- [ ] Export to different formats (JSON, Excel, Parquet)
- [ ] Query optimization suggestions
- [ ] Conversation memory (follow-up queries)
- [ ] Custom data validation rules
- [ ] Audit logging for compliance

## Creator

Built by **Sujit Sadalage** — AI & Backend Engineer

- GitHub: [sujit1661](https://github.com/sujit1661)
- Email: sujitsadalage@email.com
- Portfolio: SQL Studio AI

## License

This project is intended for learning and educational purposes. Feel free to fork, modify, and build upon it.

---

**Last updated**: August 2026  
**Version**: 1.0.0  
**Status**: Production-ready ✅
