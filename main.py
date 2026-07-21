from fastapi import FastAPI

from database import engine, Base
from routers import student, health

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="Student CRUD API using SQLAlchemy",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(student.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Student Management API"
    }