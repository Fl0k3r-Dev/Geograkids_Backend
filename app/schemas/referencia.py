from pydantic import BaseModel

class ReferenciaSchema(BaseModel):
    titulo: str
    autor: str
    descricao: str 
    referencia: str 
    link: str
