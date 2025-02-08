from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {1: 'Имя: Example, Возраст: 18'}


@app.get('/users')
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def post_user(username: str, age: int):
    user_id = len(users) + 1
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"