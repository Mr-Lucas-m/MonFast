#app/model/models.py
# coding: utf-8
from sqlalchemy import Column, Integer, String, DateTime ,ForeignKey
from sqlalchemy.orm import relationship
from db.connection import Base

# tabela de Unidades fisicas 
class Filial(Base):
    __tablename__ = 'filiais'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    estado = Column(String, index=True)
    tipo_link = Column(String, index=True)
    
    #relacao com conexoes 1:N
    # A filial pode ter várias conexões, mas cada conexão pertence a uma única filial rsrs 
    conexoes = relationship(
        "Conexao",
        back_populates="filial",
        cascade="all, delete-orphan"
        )

# tabela de conexoes IPs monitorados
class Conexao(Base):
    __tablename__ = 'conexoes'
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, index=True)
    filial_id = Column(Integer, ForeignKey('filiais.id'))
    # Relacionamento reverso com Filial
    # Cada conexão pertence a uma única filial, mas uma filial pode ter várias conexões
    filial = relationship("Filial", back_populates="conexoes")
    # relacionamento com logs (1:N)
    logs = relationship("Log", back_populates="conexao", cascade="all, delete-orphan")

# Logs de status das conexões
class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True)  # "online" ou "offline"
    timestamp = Column(DateTime, index=True)
    conexao_id = Column(Integer, ForeignKey('conexoes.id'))

    # Relacionamento reverso com conexão 1:N
    # Cada log pertence a uma única conexão, mas uma conexão pode ter vários logs
    conexao = relationship("Conexao", back_populates="logs")