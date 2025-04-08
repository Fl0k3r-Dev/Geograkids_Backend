from pydantic import BaseModel

class CartografiasSchema(BaseModel, from_attributes=True):
    titulo: str
    descricao: str
    link: str