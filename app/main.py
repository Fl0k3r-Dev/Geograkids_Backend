from fastapi import FastAPI, Depends, HTTPException
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



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1", "http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/usuario/")
def criar_usuario(usuario: UsuarioSchema, db: Session = Depends(get_db)):
    return crud_usuario.create(db, usuario)

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
def criar_referencia(referencia: ReferenciaSchema, db: Session = Depends(get_db)):
    return crud_referencia.create(db, referencia)

@app.get("/referencias/")
def listar_referencias(db: Session = Depends(get_db)):
    return crud_referencia.get_all(db)

@app.get("/referencias/{referencia_id}")
def obter_usuario(referencia_id: int, db: Session = Depends(get_db)):
    return crud_referencia.get(db, referencia_id)

@app.put("/referencias/{referencia_id}")
def atualizar_referencias(referencia_id: int, referencia: ReferenciaSchema, db: Session = Depends(get_db)):
    return crud_referencia.update(db, referencia_id, referencia)

@app.delete("/referencias/{referencia_id}")
def deletar_referencias(referencia_id: int, db: Session = Depends(get_db)):
    return crud_referencia.delete(db, referencia_id)



@app.post("/livros/")
def criar_livros(livros: LivroSchema, db: Session = Depends(get_db)):
    return crud_livros_vida.create(db, livros)

@app.get("/livros/")
def listar_livros(db: Session = Depends(get_db)):
    return crud_livros_vida.get_all(db)

@app.get("/livros/{livro_id}")
def obter_livros(livro_id: int, db: Session = Depends(get_db)):
    return crud_livros_vida.get(db, livro_id)

@app.put("/livros/{livro_id}")
def atualizar_livros(livro_id: int, livro: LivroSchema, db: Session = Depends(get_db)):
    return crud_livros_vida.update(db, livro_id, livro)

@app.delete("/livros/{livro_id}")
def deletar_livros(livro_id: int, db: Session = Depends(get_db)):
    return crud_livros_vida.delete(db, livro_id)




@app.post("/fotos/")
def criar_fotos(fotos: FotoSchema, db: Session = Depends(get_db)):
    return crud_foto.create(db, fotos)

@app.get("/fotos/")
def listar_fotos(db: Session = Depends(get_db)):
    return crud_foto.get_all(db)

@app.get("/fotos/{foto_id}")
def obter_fotos(foto_id: int, db: Session = Depends(get_db)):
    return crud_foto.get(db, foto_id)

@app.put("/fotos/{foto_id}")
def atualizar_fotos(foto_id: int, foto: FotoSchema, db: Session = Depends(get_db)):
    return crud_foto.update(db, foto_id, foto)

@app.delete("/fotos/{foto_id}")
def deletar_fotos(foto_id: int, db: Session = Depends(get_db)):
    return crud_foto.delete(db, foto_id)


@app.post("/livrosvida/")
def criar_livros_vida(item: LivroVidaSchema, db: Session = Depends(get_db)):
    return crud_livros_vida.create(db, item)

@app.get("/livrosvida/")
def listar_livros_vida(db: Session = Depends(get_db)):
    return crud_livros_vida.get_all(db)

@app.get("/livrosvida/{item_id}")
def obter_livros_vida(item_id: int, db: Session = Depends(get_db)):
    return crud_livros_vida.get(db, item_id)

@app.put("/livrosvida/{item_id}")
def atualizar_livros_vida(item_id: int, item: LivroVidaSchema, db: Session = Depends(get_db)):
    return crud_livros_vida.update(db, item_id, item)

@app.delete("/livrosvida/{item_id}")
def deletar_livros_vida(item_id: int, db: Session = Depends(get_db)):
    return crud_livros_vida.delete(db, item_id)


# VIDEOS
@app.post("/videos/")
def criar_videos(video: VideosSchema, db: Session = Depends(get_db)):
    return crud_video.create(db, video)

@app.get("/videos/")
def listar_videos(db: Session = Depends(get_db)):
    return crud_video.get_all(db)

@app.get("/videos/{video_id}")
def obter_videos(video_id: int, db: Session = Depends(get_db)):
    return crud_video.get(db, video_id)

@app.put("/videos/{video_id}")
def atualizar_videos(video_id: int, video: VideosSchema, db: Session = Depends(get_db)):
    return crud_video.update(db, video_id, video)

@app.delete("/videos/{video_id}")
def deletar_videos(video_id: int, db: Session = Depends(get_db)):
    return crud_video.delete(db, video_id)


# FICHA ATIVIDADE
@app.post("/fichasatividades/")
def criar_ficha_atividade(item: FichasAtividadesSchema, db: Session = Depends(get_db)):
    return crud_ficha_atividade.create(db, item)

@app.get("/fichasatividades/")
def listar_ficha_atividade(db: Session = Depends(get_db)):
    return crud_ficha_atividade.get_all(db)

@app.get("/fichasatividades/{item_id}")
def obter_ficha_atividade(item_id: int, db: Session = Depends(get_db)):
    return crud_ficha_atividade.get(db, item_id)

@app.put("/fichasatividades/{item_id}")
def atualizar_ficha_atividade(item_id: int, item: FichasAtividadesSchema, db: Session = Depends(get_db)):
    return crud_ficha_atividade.update(db, item_id, item)

@app.delete("/fichasatividades/{item_id}")
def deletar_ficha_atividade(item_id: int, db: Session = Depends(get_db)):
    return crud_ficha_atividade.delete(db, item_id)


# FICHA CONTEÚDO
@app.post("/fichasconteudos/")
def criar_ficha_conteudo(item: FichasConteudosSchema, db: Session = Depends(get_db)):
    return crud_ficha_conteudo.create(db, item)

@app.get("/fichasconteudos/")
def listar_ficha_conteudo(db: Session = Depends(get_db)):
    return crud_ficha_conteudo.get_all(db)

@app.get("/fichasconteudos/{item_id}")
def obter_ficha_conteudo(item_id: int, db: Session = Depends(get_db)):
    return crud_ficha_conteudo.get(db, item_id)

@app.put("/fichasconteudos/{item_id}")
def atualizar_ficha_conteudo(item_id: int, item: FichasConteudosSchema, db: Session = Depends(get_db)):
    return crud_ficha_conteudo.update(db, item_id, item)

@app.delete("/fichasconteudos/{item_id}")
def deletar_ficha_conteudo(item_id: int, db: Session = Depends(get_db)):
    return crud_ficha_conteudo.delete(db, item_id)


# CARTOGRAFIA
@app.post("/cartografia/")
def criar_cartografia(item: CartografiasSchema, db: Session = Depends(get_db)):
    return crud_cartografia.create(db, item)

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