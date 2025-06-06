from sqlalchemy import Column, Integer, String
from ..database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), index=True)
    password = Column(String(100), unique=True, index=True)
