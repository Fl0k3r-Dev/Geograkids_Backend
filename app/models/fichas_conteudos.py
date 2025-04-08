from sqlalchemy import Column, Integer, String
from ..database import Base

class FichasConteudos(Base):
    __tablename__ = "fichas_conteudos"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    descricao = Column(String(100), unique=True, index=True)
    pdf = Column(String(100), unique=True, index=True)