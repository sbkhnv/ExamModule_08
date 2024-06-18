from fastapi import FastAPI
from auth import a_router
from crud.chairs import chairs_router
from crud.comments import comments_router
from crud.posts import posts_router
from crud.team import team_router
from crud.users import ax_router
from db.schemas import JwtModel
from fastapi_jwt_auth import AuthJWT

app = FastAPI()
app.include_router(a_router)
app.include_router(chairs_router)
app.include_router(comments_router)
app.include_router(posts_router)
app.include_router(team_router)
app.include_router(ax_router)


@AuthJWT.load_config
def get_config():
    return JwtModel()


@app.get('/')
async def root():
    return {"message": "root xabari"}


@app.get('/items')
async def read_items():
    return {'message': 'test api items'}


@app.get('/user')
async def user():
    return {'message': 'user page'}


@app.get('/user/{id}')
async def read_user(id: int):
    return {'message': f'user id = {id}'}

