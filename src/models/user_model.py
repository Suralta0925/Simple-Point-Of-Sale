from pydantic import BaseModel



class UserModel(BaseModel):
    user_id: int
    username: str
    password_hash: str
    role_name: str
    first_name: str
    last_name: str
    must_change_password : int | None

class CreateUser(BaseModel):
    username: str
    password_hash: str
    first_name: str
    last_name: str

class LoginUser(BaseModel):
    username: str
    password_hash: str