from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.database.database import engine, Base
from app.models.user import User


app = FastAPI(
    title="DocuMind AI API",
    version="1.0.0"
)

@app.on_event("startup")
def startup():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1")) # une requête qui permet de vérifier le fonctionnement de la base sans modification
        Base.metadata.create_all(bind=engine)
        print("CONNEXION À POSTGRESQL RÉUSSIE.")
        print("TABLES SQLAlchemy CRÉES/VÉRIFIÉES.")
    except SQLAlchemyError as e:
        print(f"ERREUR DE CONNEXION À POSTGRESQL : {e}")

@app.get("/")
def root():
    return {
        "message": "Bienvenue sur DocuMind AI"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "database": "ok"
    }