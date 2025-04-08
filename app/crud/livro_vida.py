from app.models.livro import Livro
from app.models.livro_vida import LivrosVida
from .base import CRUDBase

crud_livros_vida = CRUDBase(LivrosVida)