from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.connection import init_db

init_db()  # Inicializa o banco de dados ao iniciar o módulo

app_router = APIRouter()

@app_router.get("/teste")
def teste():
    return {"message": "Rota de teste funcionando!"}
    