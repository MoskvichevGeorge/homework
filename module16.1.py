from fastapi import FastAPI

app = FastAPI()



@app.get('/')
async def welcome() -> dict:
    return {'message':"Главная страница"}

@app.get("/user/admin")
async def admin_panel() -> dict:
    return {'message':'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def user(user_id: str) -> dict:
    return {'message' :f'Вы вошли как пользователь № {user_id}'}

@app.get('/user')
async def user_name(username: str, age: int) -> dict:
    return {'User' : {username}, 'age':{age}, 'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}