from pydantic import BaseModel

class FotoSchema(BaseModel, from_attributes=True):
    titulo: str
    imagem: str
    descricao: str