from fastapi import APIRouter
from models import Usuario, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota de autenticação do sistema
    """
    return {"mensagem": "Vcoê acessou a rota padrão de autenticação", "autenticado":False}

@auth_router.post("/criar")
async def criar_conta(
    nome: str,
    email: str,
    senha: str,
    telefone: str
):
    Session = sessionmaker(bind=db)
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"mensagem": "Já existe um usuário com esse e-mail"}
    else:
        novo_usuario = Usuario(
            nome,
            email,
            senha,
            telefone
        )

        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "Usuário cadastrado com sucesso"}
