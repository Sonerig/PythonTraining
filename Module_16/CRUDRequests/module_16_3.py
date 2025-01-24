from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {"1": "Имя: Example, возраст: 18"}

@app.get("/users")
async def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_new_user(username: Annotated[str, Path(max_length=20, description="Enter your name", example="UrbanName")],
                          age: Annotated[int, Path(ge=18, description="Enter your age", example='20')]) -> str:
    user_id = str(int(max(users.keys())) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=0, description="Enter user id", example="15")],
                      username: Annotated[str, Path(max_length=20, description="Enter your name", example="UrbanName")],
                      age: Annotated[int, Path(ge=18, description="Enter your age", example='20')]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=0, description="Enter user id", example="15")]):
    users.pop(str(user_id))

