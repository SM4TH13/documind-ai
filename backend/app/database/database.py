from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv() # charge les variables du fichier .env

DATABASE_URL = getenv("DATABASE_URL") # recupére l'URL de connexion à la base 

if not DATABASE_URL:
    raise ValueError("La variable DATABASE_URL n'est pas définie.")

engine = create_engine(DATABASE_URL) #création du moteur SQLAlchemy

SessionLocal = sessionmaker(
    autocommit = False, 
    autoflush = False, 
    bind = engine,
) # création des sessions de base de données

Base = declarative_base() #Classe de base pour les futurs modèles

