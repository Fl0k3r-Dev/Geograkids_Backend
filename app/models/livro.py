from sqlalchemy import Column, Integer, String
from ..database import Base

class Livro(Base):
    __tablename__ = "livros"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    autor = Column(String(100), index=True)
    descricao = Column(String(100), unique=True, index=True)
    pdf = Column(String(100), unique=True, index=True)
    caminhoPdf = Column(String(100), unique=True, index=True)