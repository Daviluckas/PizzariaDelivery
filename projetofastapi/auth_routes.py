from fastapi import APIRouter
from models import Usuario, db
from sqlalchemy.orm import sessionmaker


auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do nosso sistema.
    """
    return {"mensagem" : "Você acessou a rota padrão de autenticação", "autenticado": False}

@auth_router.post("/cria_conta")
async def criar_conta(email: str, senha: str):
    Session = sessionmaker(bind=db)
    session = Session()