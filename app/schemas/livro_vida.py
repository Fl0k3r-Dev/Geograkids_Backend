from pydantic import BaseModel

class LivroVidaSchema(BaseModel, from_attributes=True):
    titulo: str
    descricao: str
    pdf: str