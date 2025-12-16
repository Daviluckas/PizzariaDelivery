from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

# uvicorn main:app --reload, executar no terminal para rodar o código

#endpoint:

#Rest APIs
# Get -> leitura/pegar
# Post -> enviar/criar
# Put/Patch -> edição
# Delete -> deletar