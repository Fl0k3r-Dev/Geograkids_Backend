from typing import Optional
from pydantic import BaseModel, constr, HttpUrl
from enum import Enum

class TipoCategoria(str, Enum):
    LUGAR = "LUGAR"
    PAISAGEM = "PAISAGEM"
    TERRITORIO = "TERRITORIO"
    REGIAO = "REGIAO"

class CategoriaBase(BaseModel):
    titulo: constr(min_length=1, max_length=255)
    descricao: str
    tipo: TipoCategoria
    texto: Optional[str] = None

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    titulo: Optional[constr(min_length=1, max_length=255)] = None
    descricao: Optional[str] = None
    tipo: Optional[TipoCategoria] = None
    texto: Optional[str] = None

class CategoriaList(BaseModel):
    id: int
    titulo: str
    descricao: str
    tipo: TipoCategoria
    tem_texto: bool
    tem_pdf: bool
    tem_slides: bool
    tem_video: bool
    tem_foto: bool

    class Config:
        from_attributes = True

class CategoriaDetail(BaseModel):
    id: int
    titulo: str
    descricao: str
    tipo: TipoCategoria
    texto: Optional[str] = None
    pdf_url: Optional[str] = None
    slides_url: Optional[str] = None
    video_url: Optional[str] = None
    foto_url: Optional[str] = None

    class Config:
        from_attributes = True 