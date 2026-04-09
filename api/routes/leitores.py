from fastapi import APIRouter
from schemas.leitor import leitorCreate, leitorOut
from services.biblioteca_service import criar_leitor, listar_leitores

router = APIRouter(prefix="/leitores", tags=["leitores"])

@router.post("", response_model=list[LeitOut])
def get_leitores () :
    return listar_leitores(data)

@router.get("", response_model=list[leitorOut])
def get_leitores () :
    return listar_leitores()