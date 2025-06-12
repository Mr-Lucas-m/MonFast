#app/schema/conexao_schem.py
from pydantic import BaseModel

class ConexaoBase(BaseModel):
    id: int
    ip: str
    filial_id: int
    class Config:
        from_attributes = True

class ConexaoCreate(BaseModel):
    ip: str
    filial_id: int

class ConexaoUpdate(BaseModel):
    ip: str | None = None
    filial_id: int | None = None
    
class ConexaoDelete(BaseModel):
    id: int
    
    class Config:
        from_attributes = True   

# obter conexoes por filial
class ConexaoRead(BaseModel):
    id: int
    ip: str
    filial_id: int

    class Config:
        from_attributes = True
