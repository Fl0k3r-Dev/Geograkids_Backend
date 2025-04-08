from sqlalchemy import Column, Integer, String
from ..database import Base

class Referencia(Base):
    __tablename__ = "referencias"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    autor = Column(String(100), unique=True, index=True)
    descricao = Column(String(100), unique=True, index=True)
    referencia = Column(String(100), unique=True, index=True)
    link = Column(String(100), unique=True, index=True)