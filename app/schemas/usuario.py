from pydantic import BaseModel

class UsuarioSchema(BaseModel, from_attributes=True):
    nome: str
    email: str

