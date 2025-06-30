from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import UploadFile, HTTPException
import os
import shutil
from datetime import datetime

from app.models.categorias import Categoria
from app.schemas.categorias import CategoriaCreate, CategoriaUpdate
from app.crud.base import CRUDBase

class CRUDCategoria(CRUDBase[Categoria, CategoriaCreate, CategoriaUpdate]):
    def get_by_titulo(self, db: Session, *, titulo: str) -> Optional[Categoria]:
        return db.query(Categoria).filter(Categoria.titulo == titulo).first()

    def create_with_files(
        self,
        db: Session,
        *,
        obj_in: CategoriaCreate,
        pdf_file: Optional[UploadFile] = None,
        slides_file: Optional[UploadFile] = None,
        video_file: Optional[UploadFile] = None,
        foto_file: Optional[UploadFile] = None
    ) -> Categoria:
        # Verificar se título já existe
        if self.get_by_titulo(db, titulo=obj_in.titulo):
            raise HTTPException(status_code=400, detail="Título já existe")

        # Criar diretório base para uploads se não existir
        upload_dir = "uploads/categorias"
        os.makedirs(upload_dir, exist_ok=True)

        # Gerar timestamp único para os arquivos
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Função auxiliar para salvar arquivo
        def save_file(file: Optional[UploadFile], prefix: str) -> Optional[str]:
            if not file:
                return None
            
            filename = f"{prefix}_{timestamp}_{file.filename}"
            file_path = os.path.join(upload_dir, filename)
            
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            return file_path

        # Salvar arquivos
        pdf_path = save_file(pdf_file, "pdf")
        slides_path = save_file(slides_file, "slides")
        video_path = save_file(video_file, "video")
        foto_path = save_file(foto_file, "foto")

        # Criar objeto do modelo
        db_obj = Categoria(
            titulo=obj_in.titulo,
            descricao=obj_in.descricao,
            tipo=obj_in.tipo,
            texto=obj_in.texto,
            pdf_path=pdf_path,
            slides_path=slides_path,
            video_path=video_path,
            foto_path=foto_path
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update_with_files(
        self,
        db: Session,
        *,
        db_obj: Categoria,
        obj_in: CategoriaUpdate,
        pdf_file: Optional[UploadFile] = None,
        slides_file: Optional[UploadFile] = None,
        video_file: Optional[UploadFile] = None,
        foto_file: Optional[UploadFile] = None
    ) -> Categoria:
        # Verificar se novo título já existe (se título for atualizado)
        if obj_in.titulo and obj_in.titulo != db_obj.titulo:
            if self.get_by_titulo(db, titulo=obj_in.titulo):
                raise HTTPException(status_code=400, detail="Título já existe")

        # Função auxiliar para atualizar arquivo
        def update_file(
            file: Optional[UploadFile],
            current_path: Optional[str],
            prefix: str
        ) -> Optional[str]:
            if not file:
                return current_path

            # Remover arquivo antigo se existir
            if current_path and os.path.exists(current_path):
                os.remove(current_path)

            # Salvar novo arquivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{prefix}_{timestamp}_{file.filename}"
            file_path = os.path.join("uploads/categorias", filename)

            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            return file_path

        # Atualizar arquivos
        pdf_path = update_file(pdf_file, db_obj.pdf_path, "pdf")
        slides_path = update_file(slides_file, db_obj.slides_path, "slides")
        video_path = update_file(video_file, db_obj.video_path, "video")
        foto_path = update_file(foto_file, db_obj.foto_path, "foto")

        # Atualizar campos do modelo
        update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)

        # Atualizar caminhos dos arquivos
        db_obj.pdf_path = pdf_path
        db_obj.slides_path = slides_path
        db_obj.video_path = video_path
        db_obj.foto_path = foto_path

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> Categoria:
        obj = db.query(Categoria).get(id)
        if not obj:
            raise HTTPException(status_code=404, detail="Categoria não encontrada")

        # Remover arquivos
        for path in [obj.pdf_path, obj.slides_path, obj.video_path, obj.foto_path]:
            if path and os.path.exists(path):
                os.remove(path)

        db.delete(obj)
        db.commit()
        return obj

crud_categoria = CRUDCategoria(Categoria) 