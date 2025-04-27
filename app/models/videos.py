from sqlalchemy import Column, Integer, String
from ..database import Base

class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), index=True)
    descricao = Column(String(100))
    video = Column(String(255))
    caminhoVideo = Column(String(255))