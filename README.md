This project provides an asynchronous FastAPI-based API for performing three mathematical operations: power, factorial, and Fibonacci. Each operation is handled by a dedicated background worker using asyncio.Queue, allowing non-blocking request processing.

The API receives input through Pydantic models, ensuring type-safe validation. Once a request is received, it is placed in the appropriate queue. Background worker coroutines continuously process tasks from these queues and return results via asyncio.Future objects. All completed operations are logged asynchronously to a SQLite database using aiosqlite.

The project follows an object-oriented design for modularity, separating concerns across services (MathService), persistence (Database), workers (workers), and routing logic.

Adressing the restrictions for the project:
1. Use a micro framework -> the project uses FastAPI
2. Follow Microservices Best Practices (MVC/MVCS) -> the project follows a modular structure by separating the code as follows:
    -models.py (Pydantic models like PowerInput, FibonacciInput)
    -routes.py (FastAPI route handlers)
    -math_service.py (contains MathService)
    -db.py handles database interactions
3. Use any API standard except SOAP -> the project uses RESTful POST endpoints
4. Consider an implementation that supports extensibility 
    -Each operation is modular, it is easy to add new math functions 
    -Routes, services, and models are all independently manageable
5. Use any SQL or NoSQL DB — SQLite is acceptable -> the project uses SQLite

How to run the project

Install dependencies:
pip install fastapi uvicorn aiosqlite pydantic

How to start server:
uvicorn main:app --reload

Access : http://localhost:8000/docs -> to test

Run the view_logs script to view the database log entries