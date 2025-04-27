from sqlalchemy import Column, Integer, String
from ..database import Base

class Foto(Base):
    __tablename__ = "fotos"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    imagem = Column(String(100), index=True)
    descricao = Column(String(100), unique=True, index=True)
    caminhoImagem = Column(String(100), unique=True, index=True)