from typing import Optional
from pydantic import BaseModel

class FichasAtividadesSchema(BaseModel, from_attributes=True):
    titulo: str
    descricao: str
    pdf: Optional[str] = None
    caminhoPdf: Optional[str] = None