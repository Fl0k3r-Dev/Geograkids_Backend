from typing import Optional
from fastapi import UploadFile
from pydantic import BaseModel

class FichasConteudosSchema(BaseModel, from_attributes=True):
    titulo: str
    descricao: str
    pdf: Optional[str] = None
    caminhoPdf: Optional[str] = None