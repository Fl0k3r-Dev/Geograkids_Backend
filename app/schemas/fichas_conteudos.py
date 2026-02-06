from typing import Optional
from fastapi import UploadFile
from pydantic import BaseModel

class FichasConteudosSchema(BaseModel):
    titulo: str
    descricao: str
    pdf: Optional[str] = None
    caminhoPdf: Optional[str] = None