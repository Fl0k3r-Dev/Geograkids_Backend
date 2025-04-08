from pydantic import BaseModel

class VideosSchema(BaseModel, from_attributes=True):
    titulo: str
    descricao: str
    video: str