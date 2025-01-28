from pydantic import BaseModel
from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates("templates")
users = list()

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/")
async def get_all_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: Annotated[int, Path(ge=0, description="Enter user id", example="15")]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(404, "User was not found")

@app.post("/user/{username}/{age}")
async def create_new_user(username: Annotated[str, Path(max_length=20, description="Enter your name", example="UrbanName")],
                          age: Annotated[int, Path(ge=18, description="Enter your age", example='20')]) -> str:
    users.append(User(id=users[-1].id+1 if users else 1, username=username, age=age))
    return f"User '{users[-1].username}' is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=0, description="Enter user id", example="15")],
                      username: Annotated[str, Path(max_length=20, description="Enter your name", example="UrbanName")],
                      age: Annotated[int, Path(ge=18, description="Enter your age", example='20')]) -> str:
    for user in users:
        if user.id == user_id:
            user.username, user.age = username, age
            return f"The user {user.username} is updated"
    raise HTTPException(404, "User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=0, description="Enter user id", example="15")]):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return f"The user {user.username} is deleted"
    raise HTTPException(404, "User was not found")

