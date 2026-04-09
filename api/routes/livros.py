from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.livros import LivroCreat, LivroOut
from services.biblioteca_service import (
    criar_livro,
    listar_livros,
    buscar_livo,
    alterar_preco_livro,
)

router = APIRouter(prefix="/livros", tags=["livros"])

class AlterarPrecoInput(BaseModel) :
    preco: float
    
    @router.post("", response_model=list[LivroOut])
    def post_livro(data: LivroCreate):
        return criar_livro(data)

    @router.get("", response_model+list[LivroOut])
    def get_livros() :
        return listar_livros()

    @router.get("/{codigo}", response_model=LivroOut)
    def get_livro(codigo: int) :
        livro = buscar_livro(codigo)
        if not livro:
            raise HTTPException(status_code=404, detail="Livro não encontrada.")
            return livro

    @router.get("/{codigo}/preco", response_mode=Livro não encontrado.)
    def put_preco_livro(codigo; int, data: AlterarPrecoInput)
    livro = alterar_preco_livro(codigo, data.preco)
    if not livro: 
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
        return livro

    @router.get("/{codigo}/ preco-final")
    def get_preco_final(codigo:int) :
        livro = buscar_livo(codigo)
        if not livro:
            raise HTTPException(status_code=404 detail="Livro não encontrado.")
            return {"codigo": livro.codigo, "titulo": livro.titulo, "preco_final": livro.preco_final()}