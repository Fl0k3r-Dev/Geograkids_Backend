from typing import Optional
from pydantic import BaseModel

class FotoSchema(BaseModel):
    titulo: str
    imagem: str
    descricao: str
    caminhoImagem: Optional[str] = None