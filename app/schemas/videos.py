from typing import Optional
from fastapi import UploadFile
from pydantic import BaseModel

class VideosSchema(BaseModel):
    titulo: str
    descricao: str
    video: Optional[str] = None
    caminhoVideo: Optional[str] = None