from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Type, TypeVar, Generic
from pydantic import BaseModel
from ..database import Base

T = TypeVar("T", bound=Base)

class CRUDBase(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    def create(self, db: Session, obj_in: BaseModel):
        obj = self.model(**obj_in.dict())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def get(self, db: Session, obj_id: int):
        obj = db.query(self.model).filter(self.model.id == obj_id).first()
        if not obj:
            raise HTTPException(status_code=404, detail="Objeto não encontrado")
        return obj

    def update(self, db: Session, obj_id: int, obj_in: BaseModel):
        obj = db.query(self.model).filter(self.model.id == obj_id).first()
        if not obj:
            raise HTTPException(status_code=404, detail="Objeto não encontrado")
        for key, value in obj_in.dict().items():
            setattr(obj, key, value)
        db.commit()
        return obj

    def delete(self, db: Session, obj_id: int):
        obj = db.query(self.model).filter(self.model.id == obj_id).first()
        if not obj:
            raise HTTPException(status_code=404, detail="Objeto não encontrado")
        db.delete(obj)
        db.commit()
        return {"message": "Objeto deletado com sucesso"}
    