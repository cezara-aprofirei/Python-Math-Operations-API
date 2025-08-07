This project provides an asynchronous FastAPI-based API for performing three mathematical operations: power, factorial, and Fibonacci. Each operation is handled by a dedicated background worker using asyncio.Queue, allowing non-blocking request processing.

The API receives input through Pydantic models, ensuring type-safe validation. Once a request is received, it is placed in the appropriate queue. Background worker coroutines continuously process tasks from these queues and return results via asyncio.Future objects. All completed operations are logged asynchronously to a SQLite database using aiosqlite.

The project follows an object-oriented design for modularity, separating concerns across services (MathService), persistence (Database), workers (workers), and routing logic.

Install dependencies:

pip install fastapi uvicorn aiosqlite pydantic

How to start server:
uvicorn main:app --reload

Access : http://localhost:8000/docs -> to test

Run the view_logs script to view the database log entries