from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def root() -> str:
    return "Главная страница"

@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example="1")]) -> str:
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user/{username}/{age}")
async def username_age(username: Annotated[str, Path(min_length=10, max_length=20, description="Enter username", example="UrbanUser")],
                       age: Annotated[int, Path(ge=18, le=120, description="Enter age", example='24')]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
