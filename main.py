from fastpt import FastAPI
from api.routes.leitores import router as leitores_router
from api.routes.livros import router as livros_router

app = FastAPI(title="Biblioteca API")

@app.get("/")
def home() :
    return{"msg": "Biblioteca API cucionando"}

app.include_router(leitores_router)
app.include_router (livros_router)