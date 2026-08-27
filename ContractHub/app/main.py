from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.database import engine, Base, SessionLocal
from app.models.models import Empresa
from app.schemas import CriarEmpresa


app = FastAPI(
    title=" Contract Hub",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "Contract Hub API funcionando!"
    }


@app.get("/test-db")
def test_database():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

    return {
        "database": "conectado",    
        "result": result.scalar()
    }

@app.post("/empresas")
def criar_empresa(dados: CriarEmpresa):

    db = SessionLocal()

    nova_empresa = Empresa(
        nome=dados.nome,
        cnpj=dados.cnpj,
        email=dados.email,
        senha=dados.senha,
        responsavel=dados.responsavel,
        telefone=dados.telefone,
        ramo=dados.ramo
    )

    db.add(nova_empresa)
    db.commit()
    db.refresh(nova_empresa)
    db.close()

    return {
        "mensagem": "Empresa cadastrada com sucesso!",
        "id": nova_empresa.id
    }
