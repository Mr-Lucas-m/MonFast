# app/schema/relatorio_schem.py
from pydantic import BaseModel
from datetime import datetime

class ConexaoStatusOut(BaseModel):
    filial_id: int
    filial_nome: str
    estado: str
    tipo_link: str
    conexao_ip: str
    status: str  # "online" ou "offline"
    ultimo_log: datetime
