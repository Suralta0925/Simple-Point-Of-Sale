from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    password_hash: str
    first_name: str
    last_name: str
