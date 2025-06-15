#app/schema/filial_schem.py
from pydantic import BaseModel
from app.schema.conexao_schem import ConexaoBase
from typing import List, Optional

class FilialBase(BaseModel):
    id: int
    nome: str
    estado: str
    tipo_link: str

    class Config:
        from_attributes = True

class FilialCreate(BaseModel):
    nome: str
    estado: str
    tipo_link: str

    
class FilialUpdate(BaseModel):
    nome: str | None = None
    estado: str | None = None
    tipo_link: str | None = None
    
class FilialDelete(BaseModel):
    id: int
    
    class Config:
        from_attributes = True

class FilialRead(FilialBase):
    conexoes: Optional[List[ConexaoBase]] = []  # Lista de conexões associadas à filial
    
    class Config:
        from_attributes = True    