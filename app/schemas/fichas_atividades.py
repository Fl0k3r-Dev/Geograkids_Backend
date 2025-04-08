from pydantic import BaseModel

class FichasAtividadesSchema(BaseModel, from_attributes=True):
    titulo: str
    descricao: str
    pdf: str