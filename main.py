from fastapi import FastAPI 
from auth_routes import auth_router
from order_routes import order_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)

#Parte que roda o código -- executar no terminal
#uvicorn main:app --reload
