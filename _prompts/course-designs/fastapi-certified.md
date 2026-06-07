# FastAPI — Course Design
Generated: 2026-06-07

```
COURSE_TYPE:      notebook
COURSE_ID:        fastapi-certified
COURSE_FULL_NAME: FastAPI for Python Engineers
ICON:             FA
ACCENT_COLOR:     #009688
ACCENT_LIGHT:     #E0F2F1
ACCENT_DARK:      #00695C
ACCENT_DARK_DIM:  #001A17
PROVIDER:         FastAPI (Self-paced)
COST:             Free
TOTAL_DAYS:       14
DIFFICULTY:       Intermediate
TAGS:             Python, APIs, Web, Backend
EXAM_LINK:        https://fastapi.tiangolo.com/
EXAM_QUESTIONS:   null
EXAM_MINUTES:     null
EXAM_PASS_SCORE:  N/A
EXAM_NOTES:       No formal exam. Complete all 14 days and the capstone REST API to demonstrate proficiency.

NOTEBOOKS:
  day-01-quickstart
  day-02-path-query-body
  day-03-pydantic-validation
  day-04-response-models
  day-05-dependency-injection
  day-06-crud-in-memory
  day-07-sqlalchemy-database
  day-08-authentication-jwt
  day-09-background-tasks-middleware
  day-10-testing-testclient
  day-11-file-uploads-forms
  day-12-websockets
  day-13-deployment-docker
  day-14-capstone-rest-api

DAYS:
  Day 1:
    Title: FastAPI Quickstart — Your First API in 10 Lines
    Badge: learn
    Tasks:
      - {text: "Read the FastAPI introduction and features overview", url: "https://fastapi.tiangolo.com/"}
      - Install FastAPI and uvicorn: pip install fastapi uvicorn[standard]
      - Write a minimal FastAPI app with GET / that returns {"message": "Hello World"}
      - {text: "Read about automatic interactive docs (Swagger UI and ReDoc)", url: "https://fastapi.tiangolo.com/features/"}
      - Add a second route GET /items/{item_id} that returns the item_id as JSON
      - Run the app with uvicorn app:app --reload and observe hot-reload on file save
    Resources:
      - {text: "FastAPI — First Steps", url: "https://fastapi.tiangolo.com/tutorial/first-steps/"}
      - {text: "FastAPI Features Overview", url: "https://fastapi.tiangolo.com/features/"}
      - {text: "Uvicorn ASGI Server Docs", url: "https://www.uvicorn.org/"}
    Tip: "FastAPI auto-generates /docs (Swagger UI) and /redoc from your route definitions. You get interactive API documentation for free — no extra configuration needed."
    hasScore: false

  Day 2:
    Title: Path, Query, and Body Parameters
    Badge: learn
    Tasks:
      - {text: "Read the FastAPI path parameters documentation", url: "https://fastapi.tiangolo.com/tutorial/path-params/"}
      - Define a route with a typed path parameter: GET /users/{user_id: int}
      - {text: "Read about query parameters and defaults", url: "https://fastapi.tiangolo.com/tutorial/query-params/"}
      - Add optional query parameters with default values: GET /items?skip=0&limit=10
      - {text: "Read about request body with Pydantic", url: "https://fastapi.tiangolo.com/tutorial/body/"}
      - Create a POST route that accepts a JSON body and echoes it back
      - Combine path + query + body in a single PUT /items/{item_id} route
    Resources:
      - {text: "FastAPI Path Parameters", url: "https://fastapi.tiangolo.com/tutorial/path-params/"}
      - {text: "FastAPI Query Parameters", url: "https://fastapi.tiangolo.com/tutorial/query-params/"}
      - {text: "FastAPI Request Body", url: "https://fastapi.tiangolo.com/tutorial/body/"}
    Tip: "FastAPI uses Python type hints as the single source of truth for parameter types, validation, serialization, and documentation. Declare once — get everything automatically."
    hasScore: false

  Day 3:
    Title: Pydantic Models — Validation and Serialization
    Badge: learn
    Tasks:
      - {text: "Read the FastAPI Pydantic models tutorial", url: "https://fastapi.tiangolo.com/tutorial/body/"}
      - Define a Pydantic BaseModel with required and optional fields
      - Add field-level validation: min_length, ge, le, regex constraints
      - {text: "Read about nested models and model composition", url: "https://fastapi.tiangolo.com/tutorial/body-nested-models/"}
      - Define a nested model (e.g. Order containing a list of LineItem objects)
      - Use model.model_dump() and model.model_validate() to convert to/from dicts
      - {text: "Explore Pydantic v2 validators and @field_validator", url: "https://docs.pydantic.dev/latest/concepts/validators/"}
    Resources:
      - {text: "FastAPI Pydantic Models", url: "https://fastapi.tiangolo.com/tutorial/body/"}
      - {text: "FastAPI Nested Models", url: "https://fastapi.tiangolo.com/tutorial/body-nested-models/"}
      - {text: "Pydantic v2 Validators", url: "https://docs.pydantic.dev/latest/concepts/validators/"}
    Tip: "Pydantic v2 is 5–50× faster than v1 (Rust core). Use model_config = ConfigDict(strict=True) to prevent silent type coercion — you'll catch bugs at API boundaries instead of deep in business logic."
    hasScore: false

  Day 4:
    Title: Response Models and Status Codes
    Badge: practice
    Tasks:
      - {text: "Read the FastAPI response model documentation", url: "https://fastapi.tiangolo.com/tutorial/response-model/"}
      - Add response_model= to a GET route to filter output fields (e.g. strip password from UserOut)
      - Use response_model_exclude_unset=True to avoid sending null fields in responses
      - {text: "Read about status codes in FastAPI", url: "https://fastapi.tiangolo.com/tutorial/response-status-code/"}
      - Return HTTP 201 for POST, 204 for DELETE using status_code=
      - {text: "Read about HTTPException for error responses", url: "https://fastapi.tiangolo.com/tutorial/handling-errors/"}
      - Raise HTTPException(status_code=404, detail="Item not found") when an item is missing
      - Add a custom exception handler with @app.exception_handler() for a domain exception
    Resources:
      - {text: "FastAPI Response Model", url: "https://fastapi.tiangolo.com/tutorial/response-model/"}
      - {text: "FastAPI Status Codes", url: "https://fastapi.tiangolo.com/tutorial/response-status-code/"}
      - {text: "FastAPI Error Handling", url: "https://fastapi.tiangolo.com/tutorial/handling-errors/"}
    Tip: "Use response_model= to control exactly what leaves your API — never accidentally expose internal fields. Declare a separate UserOut model that inherits from UserBase but omits password_hash."
    hasScore: false

  Day 5:
    Title: Dependency Injection — Clean, Testable APIs
    Badge: practice
    Tasks:
      - {text: "Read the FastAPI dependency injection tutorial", url: "https://fastapi.tiangolo.com/tutorial/dependencies/"}
      - Create a simple dependency function get_db() that yields a database session
      - Inject it into a route with Depends(get_db) and verify it is called per request
      - {text: "Read about sub-dependencies and dependency trees", url: "https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/"}
      - Create a get_current_user dependency that reads an Authorization header
      - Chain dependencies: get_current_active_user depends on get_current_user
      - {text: "Read about class-based dependencies with __init__ + __call__", url: "https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/"}
      - Replace a function dependency with a class-based one and inject it the same way
    Resources:
      - {text: "FastAPI Dependencies", url: "https://fastapi.tiangolo.com/tutorial/dependencies/"}
      - {text: "FastAPI Sub-dependencies", url: "https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/"}
      - {text: "FastAPI Classes as Dependencies", url: "https://fastapi.tiangolo.com/tutorial/dependencies/classes-as-dependencies/"}
    Tip: "Dependency injection is FastAPI's superpower for testability. Override any dependency in tests with app.dependency_overrides[get_db] = get_test_db — no mocking frameworks needed."
    hasScore: false

  Day 6:
    Title: CRUD API with In-Memory Storage
    Badge: practice
    Tasks:
      - Design a complete Items API: POST /items, GET /items, GET /items/{id}, PUT /items/{id}, DELETE /items/{id}
      - Implement the in-memory store as a dict and a Pydantic Item model
      - Return 404 when an item is not found; 409 when a POST conflicts with an existing id
      - Use proper HTTP status codes: 201 for create, 200 for read/update, 204 for delete
      - Add pagination to GET /items with skip and limit query parameters
      - {text: "Read about APIRouter for splitting routes across files", url: "https://fastapi.tiangolo.com/tutorial/bigger-applications/"}
      - Refactor the Items routes into a separate router and include it with app.include_router()
    Resources:
      - {text: "FastAPI Path Operations", url: "https://fastapi.tiangolo.com/tutorial/path-operation-configuration/"}
      - {text: "FastAPI Bigger Applications", url: "https://fastapi.tiangolo.com/tutorial/bigger-applications/"}
      - {text: "FastAPI Query Parameters and String Validations", url: "https://fastapi.tiangolo.com/tutorial/query-params-str-validations/"}
    Tip: "Design your Pydantic models in three layers: ItemBase (shared fields), ItemCreate (input-only fields like password), ItemOut (response-only fields). This prevents accidental field leakage at every layer."
    hasScore: false

  Day 7:
    Title: Database Integration with SQLAlchemy
    Badge: practice
    Tasks:
      - {text: "Read the FastAPI SQL databases tutorial with SQLAlchemy", url: "https://fastapi.tiangolo.com/tutorial/sql-databases/"}
      - Set up an async SQLAlchemy engine with aiosqlite for a SQLite database
      - Define an ORM model (User, Item) using DeclarativeBase
      - Create a get_db dependency that yields an AsyncSession and closes it after the request
      - Implement CRUD functions: create_item, get_item, list_items, update_item, delete_item
      - Wire the CRUD functions into FastAPI routes using Depends(get_db)
      - Run Alembic migrations to create the schema without dropping existing data
    Resources:
      - {text: "FastAPI SQL Databases", url: "https://fastapi.tiangolo.com/tutorial/sql-databases/"}
      - {text: "SQLAlchemy Async Docs", url: "https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html"}
      - {text: "Alembic — Database Migrations", url: "https://alembic.sqlalchemy.org/en/latest/"}
    Tip: "Always use AsyncSession for FastAPI — synchronous sessions block the event loop. Pair SQLAlchemy 2.0+ with aiosqlite (local) or asyncpg (Postgres) and you get truly non-blocking DB calls."
    hasScore: false

  Day 8:
    Title: Authentication — OAuth2, Password Hashing, and JWT
    Badge: review
    Tasks:
      - {text: "Read the FastAPI security overview — OAuth2, Bearer tokens", url: "https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/"}
      - Install python-jose and passlib: pip install python-jose[cryptography] passlib[bcrypt]
      - Hash a password with passlib CryptContext and verify it
      - Create a /token endpoint that accepts form data, validates credentials, and returns a JWT
      - Implement get_current_user dependency that decodes the JWT from the Authorization header
      - Protect an endpoint with Depends(get_current_user) and verify 401 is returned for invalid tokens
      - Add token expiry and verify that expired tokens are rejected
    Resources:
      - {text: "FastAPI OAuth2 with JWT Tokens", url: "https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/"}
      - {text: "FastAPI Security First Steps", url: "https://fastapi.tiangolo.com/tutorial/security/first-steps/"}
      - {text: "Passlib Password Hashing", url: "https://passlib.readthedocs.io/en/stable/"}
    Tip: "Store only the hashed password — never the plaintext. Use passlib's CryptContext with schemes=['bcrypt'] and verify with .verify(plain, hashed). bcrypt includes a random salt automatically."
    hasScore: false

  Day 9:
    Title: Background Tasks, Middleware, and CORS
    Badge: review
    Tasks:
      - {text: "Read the FastAPI background tasks documentation", url: "https://fastapi.tiangolo.com/tutorial/background-tasks/"}
      - Add a BackgroundTasks parameter to a POST route and fire a task (e.g. send a welcome email log)
      - Verify the response returns immediately — the background task runs after the response is sent
      - {text: "Read about middleware in FastAPI", url: "https://fastapi.tiangolo.com/tutorial/middleware/"}
      - Add a custom request-timing middleware with @app.middleware("http") that logs request duration
      - {text: "Read the FastAPI CORS middleware documentation", url: "https://fastapi.tiangolo.com/tutorial/cors/"}
      - Add CORSMiddleware to allow a specific frontend origin and verify preflight OPTIONS returns correct headers
      - Add GZipMiddleware and verify compressed responses for large payloads
    Resources:
      - {text: "FastAPI Background Tasks", url: "https://fastapi.tiangolo.com/tutorial/background-tasks/"}
      - {text: "FastAPI Middleware", url: "https://fastapi.tiangolo.com/tutorial/middleware/"}
      - {text: "FastAPI CORS", url: "https://fastapi.tiangolo.com/tutorial/cors/"}
    Tip: "BackgroundTasks is ideal for fire-and-forget work (email, audit log, cache invalidation) that doesn't affect the response. For truly heavy work (video encoding, ML inference), use a task queue like Celery or ARQ instead."
    hasScore: false

  Day 10:
    Title: Testing with TestClient and pytest
    Badge: review
    Tasks:
      - {text: "Read the FastAPI testing documentation", url: "https://fastapi.tiangolo.com/tutorial/testing/"}
      - Install httpx and pytest: pip install httpx pytest pytest-asyncio
      - Create a TestClient from your FastAPI app and write a test for GET /
      - Write tests for POST /items (happy path, validation error, duplicate)
      - Override the get_db dependency with a test database using app.dependency_overrides
      - Use pytest fixtures to set up and tear down the test database
      - {text: "Read about async test clients with AsyncClient", url: "https://fastapi.tiangolo.com/advanced/async-tests/"}
      - Write an async test using AsyncClient + pytest.mark.asyncio for an async endpoint
    Resources:
      - {text: "FastAPI Testing", url: "https://fastapi.tiangolo.com/tutorial/testing/"}
      - {text: "FastAPI Async Tests", url: "https://fastapi.tiangolo.com/advanced/async-tests/"}
      - {text: "pytest-asyncio Documentation", url: "https://pytest-asyncio.readthedocs.io/"}
    Tip: "Use app.dependency_overrides to replace get_db with get_test_db — you get isolated tests without mocking SQLAlchemy. Each test gets a fresh in-memory SQLite database seeded in the fixture."
    hasScore: false

  Day 11:
    Title: File Uploads and Form Data
    Badge: practice
    Tasks:
      - {text: "Read the FastAPI file uploads documentation", url: "https://fastapi.tiangolo.com/tutorial/request-files/"}
      - Install python-multipart: pip install python-multipart
      - Create a POST /upload endpoint that accepts a UploadFile and returns its filename and size
      - Validate the file type by checking file.content_type (allow only image/jpeg, image/png)
      - {text: "Read about form data combined with files", url: "https://fastapi.tiangolo.com/tutorial/request-form-and-files/"}
      - Accept both a form field (description: str = Form()) and a file in the same endpoint
      - Stream large file content with async for chunk in file: to avoid loading it all into memory
      - Write the uploaded file to /tmp and return its path and checksum
    Resources:
      - {text: "FastAPI Request Files", url: "https://fastapi.tiangolo.com/tutorial/request-files/"}
      - {text: "FastAPI Request Forms", url: "https://fastapi.tiangolo.com/tutorial/request-forms/"}
      - {text: "FastAPI Forms and Files", url: "https://fastapi.tiangolo.com/tutorial/request-form-and-files/"}
    Tip: "Use UploadFile over bytes for large files — UploadFile streams to a SpooledTemporaryFile (disk-backed above 1 MB) so you avoid out-of-memory errors. Call await file.read() only for small files."
    hasScore: false

  Day 12:
    Title: WebSockets — Real-Time Communication
    Badge: practice
    Tasks:
      - {text: "Read the FastAPI WebSockets tutorial", url: "https://fastapi.tiangolo.com/advanced/websockets/"}
      - Create a /ws WebSocket endpoint that echoes received messages back
      - Build a simple broadcast manager: a ConnectionManager class with connect(), disconnect(), broadcast()
      - Implement a /ws/chat/{room_id} endpoint that broadcasts messages to all clients in a room
      - {text: "Handle WebSocket disconnects gracefully with try/except WebSocketDisconnect", url: "https://fastapi.tiangolo.com/advanced/websockets/#handling-disconnections-and-multiple-clients"}
      - Test the WebSocket endpoint using the websockets library client in a notebook code cell
      - Add path parameter authentication: reject connections without a valid token query param
    Resources:
      - {text: "FastAPI WebSockets", url: "https://fastapi.tiangolo.com/advanced/websockets/"}
      - {text: "FastAPI WebSockets — Multiple Clients", url: "https://fastapi.tiangolo.com/advanced/websockets/#handling-disconnections-and-multiple-clients"}
      - {text: "websockets Python Library", url: "https://websockets.readthedocs.io/"}
    Tip: "FastAPI WebSocket endpoints share the same dependency injection system as HTTP routes. You can use Depends() inside a WebSocket handler to authenticate connections, inject database sessions, or rate-limit connections."
    hasScore: false

  Day 13:
    Title: Deployment — Uvicorn, Gunicorn, and Docker
    Badge: review
    Tasks:
      - {text: "Read the FastAPI deployment overview", url: "https://fastapi.tiangolo.com/deployment/"}
      - Configure uvicorn with workers, host, port, and log-level from environment variables
      - {text: "Read about running FastAPI with Gunicorn + UvicornWorker for multi-process serving", url: "https://fastapi.tiangolo.com/deployment/server-workers/"}
      - Write a Dockerfile: python:3.12-slim base, COPY requirements.txt, pip install, COPY app, CMD uvicorn
      - Build the Docker image locally and run it: docker build -t myapi . && docker run -p 8000:8000 myapi
      - Add a /health endpoint that returns {"status": "ok"} — used by load balancers and Kubernetes readiness probes
      - {text: "Read about HTTPS, TLS termination, and reverse proxy configuration", url: "https://fastapi.tiangolo.com/deployment/https/"}
      - Add environment-based config with pydantic-settings: BaseSettings reads from .env automatically
    Resources:
      - {text: "FastAPI Deployment Overview", url: "https://fastapi.tiangolo.com/deployment/"}
      - {text: "FastAPI Server Workers (Gunicorn)", url: "https://fastapi.tiangolo.com/deployment/server-workers/"}
      - {text: "pydantic-settings Documentation", url: "https://docs.pydantic.dev/latest/concepts/pydantic_settings/"}
    Tip: "For production: Gunicorn with UvicornWorker gives you multi-process parallelism. Rule of thumb: workers = 2 × CPU cores + 1. For containers with autoscaling, run single-worker uvicorn and let the orchestrator (Kubernetes, ECS) handle parallelism."
    hasScore: false

  Day 14:
    Title: Capstone — Build a Complete Bookmarks REST API
    Badge: exam
    Tasks:
      - Design a Bookmarks API with users, bookmarks, and tags — full data model with relationships
      - Implement JWT authentication: POST /auth/register, POST /auth/token, GET /auth/me
      - Implement bookmarks CRUD: POST /bookmarks, GET /bookmarks, GET /bookmarks/{id}, PATCH /bookmarks/{id}, DELETE /bookmarks/{id}
      - Add tag filtering: GET /bookmarks?tag=python returns only bookmarks with that tag
      - Persist data with SQLAlchemy + SQLite — users and bookmarks in separate tables with FK
      - Add full pytest suite: test auth flow, CRUD operations, and 404/401 error cases
      - Write a Dockerfile and document how to build and run it
      - {text: "Review the FastAPI advanced user guide for any missing patterns", url: "https://fastapi.tiangolo.com/advanced/"}
    Resources:
      - {text: "FastAPI Advanced User Guide", url: "https://fastapi.tiangolo.com/advanced/"}
      - {text: "FastAPI Full Example Project", url: "https://github.com/tiangolo/full-stack-fastapi-template"}
      - {text: "FastAPI Best Practices", url: "https://fastapi.tiangolo.com/tutorial/"}
    Tip: "Structure your project as: app/main.py, app/models.py (SQLAlchemy), app/schemas.py (Pydantic), app/crud.py, app/routers/. This separation of concerns makes the codebase testable and maintainable as it grows."
    hasScore: true

TOPICS:
  Topic 1:
    Name: Core Concepts
    Color: teal
    Days: 0, 1, 2, 3   # Days 1–4 (0-indexed)

  Topic 2:
    Name: Dependencies & CRUD
    Color: blue
    Days: 4, 5          # Days 5–6 (0-indexed)

  Topic 3:
    Name: Database & Auth
    Color: purple
    Days: 6, 7          # Days 7–8 (0-indexed)

  Topic 4:
    Name: Advanced Features
    Color: orange
    Days: 8, 9, 10, 11  # Days 9–12 (0-indexed)

  Topic 5:
    Name: Deployment & Testing
    Color: coral
    Days: 12            # Day 13 (0-indexed)

  Topic 6:
    Name: Capstone Project
    Color: teal
    Days: 13            # Day 14 (0-indexed)
```
