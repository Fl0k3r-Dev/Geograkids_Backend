from typing import Optional
from fastapi import File, UploadFile
from pydantic import BaseModel

class LivroSchema(BaseModel):
    titulo: str
    autor: str
    descricao: str
    pdf: Optional[str] = None
    caminhoPdf: Optional[str] = None