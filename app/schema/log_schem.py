#app/schema/log_schem.py
from pydantic import BaseModel
from datetime import datetime
   
class LogBase(BaseModel):
    id: int
    status: str
    timestamp: datetime

    class Config:
        from_attributes = True

class LogCreate(BaseModel):
    status: str
    timestamp: datetime
    conexao_id: int

# obter logs por conexao 
class LogRead(BaseModel):
    id: int
    status: str
    timestamp: datetime
    conexao_id: int
    
    class Config:
        from_attributes = True
