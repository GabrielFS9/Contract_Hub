from datetime import datetime
from app.database import Base
from sqlalchemy import Column, String, Integer, DateTime

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    responsavel = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    ramo = Column(String)
    data_cadastro = Column(DateTime, default=datetime.now)


