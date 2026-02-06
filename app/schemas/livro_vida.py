from typing import Optional
from pydantic import BaseModel

class LivroVidaSchema(BaseModel):
    titulo: str
    descricao: str
    pdf: Optional[str] = None
    caminhoPdf: Optional[str] = None