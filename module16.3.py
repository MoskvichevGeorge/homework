from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_return() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username:str, age:int) -> str:
    current_index = max(map(users.keys()), default=0)
    users[str(current_index)]= f'Имя Имя: {username}, возраст: {age}'
    return f"User {current_index} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_message(user_id: str, username: str,age: int ) -> str:
    if user_id in users:
        users[user_id] = f'Имя: {username}, возраст: {age}'
        return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: str) ->str:
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"




