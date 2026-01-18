from fastapi import APIRouter
auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota de autenticação do sistema
    """
    return {"mensagem": "Vcoê acessou a rota padrão de autenticação", "autenticado":False}
