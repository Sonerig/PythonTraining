from fastapi import FastAPI
from app.routes import user, task

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
