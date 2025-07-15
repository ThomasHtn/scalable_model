import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Chemin absolu, indépendant du dossier courant
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
DB_DIR = os.path.join(PROJECT_ROOT, "dump")
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, "generated-user.db")

# Assure-toi que le dossier 'dump/' existe
os.makedirs(DB_DIR, exist_ok=True)

print(f"📂 Utilisation de la base de données : {DB_PATH}")

# Moteur SQLAlchemy
engine = create_engine(
    f"sqlite:///{DB_PATH}", connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
