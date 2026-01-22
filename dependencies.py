from models import db
from sqlalchemy.orm import sessionmaker

#Aqui eu consigo criar a sessão no db, mandar pra rota (import), ela vai usar a sessão, se der certou ou n, entra no finally de todo jeito
def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        {"mensagem": "Sessão encerrada com sucesso"}
        session.close()