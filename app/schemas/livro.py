from pydantic import BaseModel

class LivroSchema(BaseModel, from_attributes=True):
    titulo: str
    autor: str
    descricao: str
    pdf: str