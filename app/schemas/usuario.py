from pydantic import BaseModel

class UsuarioSchema(BaseModel, from_attributes=True):
    username: str
    password: str

