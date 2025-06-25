# routers/route_result.py
from fastapi import APIRouter
from resultado.status import resultados_conexoes

router = APIRouter()

@router.get("/status")
def get_status():
    return resultados_conexoes
