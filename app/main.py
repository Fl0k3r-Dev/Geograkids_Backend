import hashlib
from pydantic import BaseModel
import sys

from starlette.staticfiles import StaticFiles
sys.path.insert(0, '/home/geografando1/public_html/meus_pacotes')
from datetime import datetime, timedelta
import os
from fastapi import FastAPI, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.usuario import crud_usuario
from app.crud.referencia import crud_referencia
from app.crud.livro import crud_livro
from app.crud.foto import crud_foto
from app.schemas.foto import FotoSchema
from app.schemas.livro import LivroSchema
from app.schemas.referencia import ReferenciaSchema
from app.schemas.usuario import UsuarioSchema
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.livro_vida import crud_livros_vida
from app.crud.videos import crud_video
from app.crud.fichas_atividades import crud_ficha_atividade
from app.crud.fichas_conteudos import crud_ficha_conteudo
from app.crud.cartografias import crud_cartografia
from app.schemas.livro_vida import LivroVidaSchema
from app.schemas.videos import VideosSchema
from app.schemas.livro_vida import LivroVidaSchema
from app.schemas.fichas_atividades import FichasAtividadesSchema
from app.schemas.fichas_conteudos import FichasConteudosSchema
from app.schemas.cartografias import CartografiasSchema
from typing import Optional
from fastapi import FastAPI, Depends, File, Form, HTTPException, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta

import sys

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI(root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode definir origens específicas, se necessário, ex: ["http://127.0.0.1"]
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

SECRET_KEY = "uma-chave-secreta-muito-forte"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 2

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginData(BaseModel):
    username: str
    password: str

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)  # aqui injetamos a sessão do banco
):
    usuario = crud_usuario.get_by_username(db, form_data.username)
    if not usuario or not comparar_md5(form_data.password, usuario.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    access_token = create_access_token(
        data={"sub": form_data.username},
        expires_delta=timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    )

    return {"access_token": access_token, "token_type": "bearer"}

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")

@app.get("/protegido")
def rota_protegida(usuario=Depends(verify_token)):
    return {"message": f"Acesso autorizado para {usuario['sub']}"}

@app.post("/usuario/")
def criar_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    usuario.password = gerar_md5(usuario.password);
    return crud_usuario.create(db, usuario)

def gerar_md5(texto: str) -> str:
    return hashlib.md5(texto.encode()).hexdigest()

def comparar_md5(texto: str, hash_md5: str) -> bool:
    return gerar_md5(texto) == hash_md5

@app.get("/usuario/")
def listar_usuarios(db: Session = Depends(get_db)):
    return crud_usuario.get_all(db)

@app.get("/usuario/{usuario_id}")
def obter_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return crud_usuario.get(db, usuario_id)

@app.put("/usuario/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario: UsuarioSchema, db: Session = Depends(get_db)):
    return crud_usuario.update(db, usuario_id, usuario)

@app.delete("/usuario/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return crud_usuario.delete(db, usuario_id)


@app.post("/referencias/")
def criar_referencia(
    titulo: str = Form(...),
    autor: str = Form(...),
    descricao: str = Form(...),
    referencia: str = Form(...),
    link: str = Form(...),
    db: Session = Depends(get_db)
):
    # montar o schema
    referencia_data = ReferenciaSchema(
        titulo=titulo,
        autor=autor,
        descricao=descricao,
        referencia=referencia,
        link=link
    )
    return crud_referencia.create(db, referencia_data)


@app.get("/referencias/")
def listar_referencias(db: Session = Depends(get_db)):
    return crud_referencia.get_all(db)

@app.put("/referencias/{referencia_id}")
def atualizar_referencia(
    referencia_id: int,
    titulo: str = Form(...),
    autor: str = Form(...),
    descricao: str = Form(...),
    referencia: str = Form(...),
    link: str = Form(...),
    db: Session = Depends(get_db)
):
    referencia_data = ReferenciaSchema(
        titulo=titulo,
        autor=autor,
        descricao=descricao,
        referencia=referencia,
        link=link
    )
    return crud_referencia.update(db, referencia_id, referencia_data)
    
@app.put("/referencias/{referencia_id}")
def atualizar_referencias(referencia_id: int, referencia: ReferenciaSchema, db: Session = Depends(get_db)):
    return crud_referencia.update(db, referencia_id, referencia)

@app.delete("/referencias/{referencia_id}")
def deletar_referencias(referencia_id: int, db: Session = Depends(get_db)):
    return crud_referencia.delete(db, referencia_id)

@app.post("/livros/")
def criar_livros(
    titulo: str = Form(...),
    autor: str = Form(...),
    descricao: str = Form(...),
    pdf: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    caminho_pdf = None
    if pdf:
        caminho_pdf = f"uploads/livros/{pdf.filename}"
        os.makedirs(os.path.dirname(caminho_pdf), exist_ok=True)
        with open(caminho_pdf, "wb") as f:
            f.write(pdf.file.read())

    livro_data = LivroSchema(
        titulo = titulo,
        autor = autor,
        descricao = descricao,
        pdf = pdf.filename,
        caminhoPdf= caminho_pdf
    )

    return crud_livro.create(db, livro_data)

@app.get("/livros/")
def listar_livros(db: Session = Depends(get_db)):
    return crud_livro.get_all(db)

@app.get("/livros/{livro_id}")
def obter_livros(livro_id: int, db: Session = Depends(get_db)):
    return crud_livro.get(db, livro_id)

@app.put("/livros/{livro_id}")
def atualizar_livros(
    livro_id: int,
    titulo: str = Form(...),
    autor: str = Form(...),
    descricao: str = Form(...),
    pdf: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    
    livro = crud_livro.get(db, livro_id)

    if livro and livro.pdf:
        caminho_arquivo = livro.caminhoPdf
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

    caminho_pdf = None
    if pdf:
        caminho_pdf = f"uploads/livros/{titulo}-{pdf.filename}"
        os.makedirs(os.path.dirname(caminho_pdf), exist_ok=True)
        with open(caminho_pdf, "wb") as f:
            f.write(pdf.file.read())

    livro_data = LivroSchema(
        titulo=titulo,
        autor=autor,
        descricao=descricao,
        pdf=pdf.filename,
        caminhoPdf=caminho_pdf
    )

    return crud_livro.update(db, livro_id, livro_data)

@app.delete("/livros/{livro_id}")
def deletar_livros(livro_id: int, db: Session = Depends(get_db)):
    livro = crud_livro.get(db, livro_id)

    if livro and livro.pdf:
        caminho_arquivo = livro.caminhoPdf

        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

    return crud_livro.delete(db, livro_id)

os.makedirs("uploads", exist_ok=True)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

@app.post("/fotos/")
def criar_fotos(
    titulo: str = Form(...),
    descricao: str = Form(...),
    imagem: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    caminho_imagem = None

    if imagem:
        caminho_imagem = f"uploads/fotos/{titulo}-{imagem.filename}"
        
        os.makedirs(os.path.dirname(caminho_imagem), exist_ok=True)
        
        with open(caminho_imagem, "wb") as f:
            f.write(imagem.file.read())

    foto_data = FotoSchema(
        titulo=titulo,
        descricao=descricao,
        imagem= imagem.filename,
        caminhoImagem=caminho_imagem
    )

    return crud_foto.create(db, foto_data)


@app.get("/fotos/")
def listar_fotos(db: Session = Depends(get_db)):
    return crud_foto.get_all(db)

@app.get("/fotos/{foto_id}")
def obter_fotos(foto_id: int, db: Session = Depends(get_db)):
    return crud_foto.get(db, foto_id)

@app.put("/fotos/{foto_id}")
def atualizar_fotos(
    foto_id: int,
    titulo: str = Form(...),
    descricao: str = Form(...),
    imagem: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    
    foto = crud_foto.get(db, foto_id)

    if foto and foto.imagem:
        caminho_arquivo = foto.caminhoImagem
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

    caminho_imagem = None
    if imagem:
        caminho_imagem = f"uploads/fotos/{titulo}-{imagem.filename}"
        os.makedirs(os.path.dirname(caminho_imagem), exist_ok=True)
        with open(caminho_imagem, "wb") as f:
            f.write(imagem.file.read())

    foto_data = FotoSchema(
        titulo=titulo,
        descricao=descricao,
        imagem=imagem.filename,
        caminhoImagem=caminho_imagem
    )

    return crud_foto.update(db, foto_id, foto_data)


@app.delete("/fotos/{foto_id}")
def deletar_fotos(foto_id: int, db: Session = Depends(get_db)):
    arquivo = crud_foto.get(db, foto_id)

    if arquivo and arquivo.imagem:
        caminho_arquivo = arquivo.caminhoImagem
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

    return crud_foto.delete(db, foto_id)


@app.post("/livrosvida/")
def criar_livro_vida(
    titulo: str = Form(...),
    descricao: str = Form(...),
    pdf: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    caminho_pdf = f"uploads/livrosvida/{titulo}-{pdf.filename}"
    
    os.makedirs(os.path.dirname(caminho_pdf), exist_ok=True)
    
    with open(caminho_pdf, "wb") as f:
        f.write(pdf.file.read())

    livro_vida_data = LivroVidaSchema(
        titulo=titulo,
        descricao=descricao,
        pdf=pdf.filename,
        caminhoPdf=caminho_pdf
    )

    return crud_livros_vida.create(db, livro_vida_data)

@app.get("/livrosvida/")
def listar_livros_vida(db: Session = Depends(get_db)):
    return crud_livros_vida.get_all(db)

@app.get("/livrosvida/{item_id}")
def obter_livros_vida(item_id: int, db: Session = Depends(get_db)):
    return crud_livros_vida.get(db, item_id)

@app.put("/livrosvida/{livro_id}")
def atualizar_livros_vida(
    livro_id: int,
    titulo: str = Form(...),
    descricao: str = Form(...),
    pdf: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    caminho_pdf = None
    if pdf:
        caminho_pdf = f"uploads/livrosvida/{titulo}-{pdf.filename}"
        os.makedirs(os.path.dirname(caminho_pdf), exist_ok=True)
        with open(caminho_pdf, "wb") as f:
            f.write(pdf.file.read())

    livro_vida_data = LivroVidaSchema(
        titulo=titulo,
        descricao=descricao,
        pdf=pdf.filename,
        caminhoPdf=caminho_pdf
    )

    return crud_livros_vida.update(db, livro_id, livro_vida_data)

@app.delete("/livrosvida/{item_id}")
def deletar_livros_vida(item_id: int, db: Session = Depends(get_db)):

    arquivo = crud_livros_vida.get(db, item_id)

    if arquivo and arquivo.pdf:
        caminho_arquivo = arquivo.caminhoPdf
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

    return crud_livros_vida.delete(db, item_id)


# VIDEOS

@app.post("/videos/")
def criar_videos(
    titulo: str = Form(...),
    descricao: str = Form(...),
    video: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    caminho_video = f"uploads/videos/{titulo}-{video.filename}"
    
    os.makedirs(os.path.dirname(caminho_video), exist_ok=True)
    
    with open(caminho_video, "wb") as f:
        f.write(video.file.read())

    video_data = VideosSchema(
        titulo=titulo,
        descricao=descricao,
        video=video.filename,
        caminhoVideo=caminho_video
    )

    return crud_video.create(db, video_data)


@app.get("/videos/")
def listar_videos(db: Session = Depends(get_db)):
    return crud_video.get_all(db)

@app.get("/videos/{video_id}")
def obter_videos(video_id: int, db: Session = Depends(get_db)):
    return crud_video.get(db, video_id)


@app.put("/videos/{video_id}")
def atualizar_videos(
    video_id: int,
    titulo: str = Form(...),
    descricao: str = Form(...),
    video: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    videoObj = crud_video.get(db, video_id)

    if video and videoObj.video:
        caminho_arquivo = videoObj.caminhoVideo
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

    caminho_video = None
    if video:
        caminho_video = f"uploads/videos/{titulo}-{video.filename}"
        os.makedirs(os.path.dirname(caminho_video), exist_ok=True)
        with open(caminho_video, "wb") as f:
            f.write(video.file.read())

    video_data = VideosSchema(
        titulo=titulo,
        descricao=descricao,
        video=video.filename,
        caminhoVideo=caminho_video
    )

    return crud_video.update(db, video_id, video_data)


@app.delete("/videos/{video_id}")
def deletar_videos(video_id: int, db: Session = Depends(get_db)):
     
    arquivo = crud_video.get(db, video_id)

    if arquivo and arquivo.video:
        caminho_arquivo = arquivo.caminhoVideo
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)
    return crud_video.delete(db, video_id)


# FICHA ATIVIDADE

@app.post("/fichasatividades")
def criar_ficha_atividade(
    titulo: str = Form(...),
    descricao: str = Form(...),
    pdf: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    caminho_arquivo = None
    if pdf:
        caminho_arquivo = f"uploads/fichasatividades/{titulo}_{pdf.filename}"
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        with open(caminho_arquivo, "wb") as f:
            f.write(pdf.file.read())

    ficha_data = FichasAtividadesSchema(
        titulo=titulo,
        descricao=descricao,
        pdf=pdf.filename,
        caminhoPdf=caminho_arquivo
    )

    return crud_ficha_atividade.create(db, ficha_data)

@app.put("/fichasatividades/{ficha_id}")
def atualizar_ficha_atividade(
    ficha_id: int,
    titulo: str = Form(...),
    descricao: str = Form(...),
    pdf: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    
    arquivoObj = crud_ficha_atividade.get(db, ficha_id)

    if pdf and arquivoObj.pdf:
        caminho_arquivo = arquivoObj.caminhoPdf
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

    caminho_arquivo = None
    if pdf:
        caminho_arquivo = f"uploads/fichasatividades/{titulo}-{pdf.filename}"
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        with open(caminho_arquivo, "wb") as f:
            f.write(pdf.file.read())

    ficha_data = FichasAtividadesSchema(
        titulo=titulo,
        descricao=descricao,
        pdf=pdf.filename,
        caminhoPdf=caminho_arquivo
    )

    return crud_ficha_atividade.update(db, ficha_id, ficha_data)

@app.get("/fichasatividades")
def listar_ficha_atividade(db: Session = Depends(get_db)):
    return crud_ficha_atividade.get_all(db)

@app.get("/fichasatividades/{item_id}")
def obter_ficha_atividade(item_id: int, db: Session = Depends(get_db)):
    return crud_ficha_atividade.get(db, item_id)

@app.delete("/fichasatividades/{item_id}")
def deletar_ficha_atividade(item_id: int, db: Session = Depends(get_db)):

    arquivo = crud_ficha_atividade.get(db, item_id)

    if arquivo and arquivo.pdf:
        caminho_arquivo = arquivo.caminhoPdf
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

    return crud_ficha_atividade.delete(db, item_id)


# FICHA CONTEÚDO

@app.post("/fichasconteudos")
def criar_ficha_conteudo(
    titulo: str = Form(...),
    descricao: str = Form(...),
    pdf: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    caminho_arquivo = f"uploads/fichasconteudos/{titulo}-{pdf.filename}"
    
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
    
    with open(caminho_arquivo, "wb") as f:
        f.write(pdf.file.read())

    ficha_data = FichasConteudosSchema(
        titulo=titulo,
        descricao=descricao,
        pdf=pdf.filename,
        caminhoPdf=caminho_arquivo
    )

    return crud_ficha_conteudo.create(db, ficha_data)

@app.get("/fichasconteudos")
def listar_ficha_conteudo(db: Session = Depends(get_db)):
    return crud_ficha_conteudo.get_all(db)

@app.get("/fichasconteudos/{item_id}")
def obter_ficha_conteudo(item_id: int, db: Session = Depends(get_db)):
    return crud_ficha_conteudo.get(db, item_id)

@app.put("/fichasconteudos/{ficha_id}")
def atualizar_fichas_conteudos(
    ficha_id: int, 
    titulo: str,
    descricao: str, 
    pdf: Optional[UploadFile] = None,
    db: Session = Depends(get_db)
):
    arquivoObj = crud_ficha_conteudo.get(db, ficha_id)

    if pdf and arquivoObj.pdf:
        caminho_arquivo = arquivoObj.caminhoPdf
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

    caminho_arquivo = None
    if pdf:
        caminho_arquivo = f"uploads/fichasconteudos/{titulo}-{pdf.filename}"
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        with open(caminho_arquivo, "wb") as f:
            f.write(pdf.file.read())

    ficha_data = FichasConteudosSchema(
        titulo=titulo,
        descricao=descricao,
        pdf=pdf.filename,
        caminhoPdf=caminho_arquivo
    )

    return crud_ficha_conteudo.update(db, ficha_id, ficha_data)

@app.delete("/fichasconteudos/{item_id}")
def deletar_ficha_conteudo(item_id: int, db: Session = Depends(get_db)):

    arquivo = crud_ficha_conteudo.get(db, item_id)

    if arquivo and arquivo.pdf:
        caminho_arquivo = arquivo.caminhoPdf
        if os.path.exists(caminho_arquivo):
            os.remove(caminho_arquivo)

    return crud_ficha_conteudo.delete(db, item_id)


# CARTOGRAFIA
@app.post("/cartografia/")
def criar_cartografia(
    titulo: str = Form(...),
    descricao: str = Form(...),
    link: str = Form(...),
    db: Session = Depends(get_db)
):
    item_dict = {"titulo": titulo, "descricao": descricao, "link": link}
    return crud_cartografia.create(db, item_dict)

@app.get("/cartografia/")
def listar_cartografia(db: Session = Depends(get_db)):
    return crud_cartografia.get_all(db)

@app.get("/cartografia/{item_id}")
def obter_cartografia(item_id: int, db: Session = Depends(get_db)):
    return crud_cartografia.get(db, item_id)

@app.put("/cartografia/{item_id}")
def atualizar_cartografia(item_id: int, item: CartografiasSchema, db: Session = Depends(get_db)):
    return crud_cartografia.update(db, item_id, item)

@app.delete("/cartografia/{item_id}")
def deletar_cartografia(item_id: int, db: Session = Depends(get_db)):
    return crud_cartografia.delete(db, item_id)
