from pydantic import BaseModel

class FichasConteudosSchema(BaseModel, from_attributes=True):
    titulo: str
    descricao: str
    pdf: str