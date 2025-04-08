from pydantic import BaseModel

class ReferenciaSchema(BaseModel, from_attributes=True):
    titulo: str
    autor: str
    descricao: str 
    referencia: str 
    link: str
