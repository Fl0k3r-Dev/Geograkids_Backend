from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    username: str
    password: str

