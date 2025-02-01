from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root():
    return ("Главная страница")


@app.get("/user/admin")
async def admin():
    return ("Вы вошли как администратор")


@app.get("/users/{user_id}")
async def get_user(user_id: Annotated[int, Path(gt=0,
                                                le=100,
                                                description='Enter User ID')], ):
    return (f"Вы вошли как пользователь №{user_id}")


@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(min_length=5,
                                                  max_length=20,
                                                  pattern="^[a-zA-Z0-9_-]+$",
                                                  description='Enter username')],
                    age: Annotated[int, Path(gt=18,
                                             le=120,
                                             description='Enter age')]):
    return (f"Информация о пользователе. Имя: {username}, Возраст: {age}")
