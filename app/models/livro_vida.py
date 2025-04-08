from sqlalchemy import Column, Integer, String
from ..database import Base

class LivrosVida(Base):
    __tablename__ = "livros_vida"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    descricao = Column(String(100), unique=True, index=True)
    pdf = Column(String(100), unique=True, index=True)