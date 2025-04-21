from pydantic import BaseModel


class createUser(BaseModel):
    username: str
    password: str

class login(createUser):
    pass

class LoginUser(BaseModel):
    username: str
    password: str