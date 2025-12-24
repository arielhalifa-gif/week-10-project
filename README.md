# week-10-project

## API Endpoints


| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | `/contacts` | Get all contacts | None |
| POST | `/contacts` | Create new contact | `{first_name, last_name, phone_number}` |
| PUT | `/contacts/{id}` | Update contact | `{first_name?, last_name?, phone_number?}` |
| DELETE | `/contacts/{id}` | Delete contact | None |

## Setup & Running

### Option 1: Docker Deployment (Production)

**Prerequisites:**
- Docker
- Docker Compose

**Steps:**

1. Clone the repository:
```bash
git clone <your-repo-url>
cd contact-manager
```

2. Configure environment for Docker:
```bash
cp .env.example .env
# Edit .env and set DB_HOST=db
```

3. Start the application:
```bash
docker compose up -d
```

4. Wait ~30 seconds for database initialization

5. Access the API:
   - API: `http://localhost:8000/contacts`
   - Docs: `http://localhost:8000/docs`

**Stopping:**
```bash
docker compose down          # Stop (preserves data)
docker compose down -v       # Stop and remove data
```

### Option 2: Local Development (with venv)

**Prerequisites:**
- Python 3.11+
- Docker (for MySQL database only)

**Steps:**

1. Start MySQL database:
```bash
docker compose up -d db
```

2. Create virtual environment:
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows
# or
source .venv/bin/activate      # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r app/requirements.txt
```

4. Configure environment for local dev:
```bash
# Ensure .env has DB_HOST=localhost
```

5. Run the server:
```bash
cd app
python main.py
```

Or with uvicorn directly:
```bash
cd app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

6. Access the API at `http://localhost:8000`

## Environment Configuration

The `.env` file configures database connection:

```bash
# For Docker deployment
DB_HOST=db              # Use Docker service name

# For local development
DB_HOST=localhost       # Connect to local MySQL

# Common settings
DB_PORT=3306
DB_USER=root
DB_PASSWORD=rootpassword
DB_NAME=contacts_db
```

**Note:** Use `DB_HOST=db` for Docker, `DB_HOST=localhost` for local development.

## Testing the API

### Using cURL

**Get all contacts:**
```bash
curl http://localhost:8000/contacts
```

**Create a contact:**
```bash
curl -X POST http://localhost:8000/contacts \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "050-1234567"
  }'
```

**Update a contact:**
```bash
curl -X PUT http://localhost:8000/contacts/1 \
  -H "Content-Type: application/json" \
  -d '{"phone_number": "052-9999999"}'
```

**Delete a contact:**
```bash
curl -X DELETE http://localhost:8000/contacts/1
```

### Using Interactive Docs

Navigate to `http://localhost:8000/docs` for Swagger UI with:
- Interactive API testing
- Request/response examples
- Schema definitions

## Data Persistence

MySQL data is stored in a Docker volume named `mysql_data`:

```bash
# View volumes
docker volume ls

# Inspect volume
docker volume inspect contact-manager_mysql_data
```

To verify persistence:
```bash
# Create a contact
curl -X POST http://localhost:8000/contacts \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Test","last_name":"User","phone_number":"050-9999999"}'

# Stop containers
docker compose down

# Restart containers
docker compose up -d
sleep 30

# Verify data persisted
curl http://localhost:8000/contacts
```

## Database Schema

**Contacts Table:**
```sql
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL UNIQUE
);
```

**Sample Data:**
4 contacts are automatically inserted on first run (see `sql/init.sql`).

## Development

**Key Design Decisions:**
- No ORM - uses raw SQL with parameterized queries
- Static methods for data access and DB connection
- Pydantic models for request/response validation
- Environment-based configuration

**Adding New Features:**
1. Define entity in `entities/`
2. Create data access layer in `data_access/`
3. Add API routes in `api.py`
4. Update database schema in `sql/init.sql`

## Troubleshooting

**API can't connect to database:**
- Check `DB_HOST` in `.env` (use `db` for Docker, `localhost` for local)
- Verify database container is running: `docker compose ps`
- Check logs: `docker compose logs db`

**Port already in use:**
- Change port mapping in `compose.yaml`: `"8001:8000"`
- Or stop conflicting service on port 8000

**Database not initializing:**
- Wait longer (~30 seconds)
- Check healthcheck: `docker compose ps`
- View logs: `docker compose logs db`

## License

[Your License Here]

## Contributors

[You