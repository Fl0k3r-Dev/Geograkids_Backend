from sqlalchemy import Column, Integer, String
from ..database import Base

class Cartografias(Base):
    __tablename__ = "cartografia"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    descricao = Column(String(100), unique=True, index=True)
    link = Column(String(100), unique=True, index=True)