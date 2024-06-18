from pydantic import BaseModel
from typing import Optional

class JwtModel(BaseModel):
    authjwt_secret_key: str = '192ba1860ccd8dcb1577983848289f3792e3c896fd7df9277a773d39d2c9e291'

class RegisterUser(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    username: str
    password: str
    email: str


class LoginUser(BaseModel):
    username: str
    password: str

class Chairs(BaseModel):
    id: Optional[int]
    image: str
    name: str
    description: str
    price: float


class Comments(BaseModel):
    id: Optional[int]
    text: str
    image: str
    first_name: str
    las_name: str
    job: str


class Posts(BaseModel):
    id: Optional[int]
    image: str
    description: str
    staff_name: str
    create_date: str


class TeamMembers(BaseModel):
    id: Optional[int]
    image: str
    first_name: str
    las_name: str
    job: str
    description: str

