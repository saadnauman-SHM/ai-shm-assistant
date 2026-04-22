from fastapi import FastAPI
from app.routes.ask import router as ask_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI SHM Assistant running 🚀"}

app.include_router(ask_router)