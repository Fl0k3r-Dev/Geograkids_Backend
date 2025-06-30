from sqlalchemy import Column, Integer, String, Enum, Text
from app.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), unique=True, nullable=False)
    descricao = Column(Text, nullable=False)
    tipo = Column(Enum('LUGAR', 'PAISAGEM', 'TERRITORIO', 'REGIAO', name='tipo_categoria'), nullable=False)
    texto = Column(Text, nullable=True)
    
    # Caminhos dos arquivos
    pdf_path = Column(String(255), nullable=True)
    slides_path = Column(String(255), nullable=True)
    video_path = Column(String(255), nullable=True)
    foto_path = Column(String(255), nullable=True) 