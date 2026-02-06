from pydantic import BaseModel

class CartografiasSchema(BaseModel):
    titulo: str
    descricao: str
    link: str