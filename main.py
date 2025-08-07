from fastapi import FastAPI
from db import Database
from workers import start_workers
from routes import router

app = FastAPI()
db = Database()


@app.on_event("startup")
async def startup_event():
    await db.init()
    await start_workers()

app.include_router(router)
