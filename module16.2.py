from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/user/{user_id}')
async def news(user_id: int = Path(de=1, le=100, description='Enter User ID', example='1')) -> dict:
    return {'message': f'Вы вошли как пользователь  id{user_id}'}


@app.get('/user/{username}/{age}')
async def news(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='Urban')],
        age: int = Path(de=18, le=120, description=' Enter your id', example='24')) -> dict:
    return {"message": f'Your name {username},your age {age}'}
