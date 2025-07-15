import os
import sys

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

# Add folder parent in PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.crud.user_crud import get_all_users
from database.db_init import SessionLocal
from database.schemas.user_schema import UserOut

app = FastAPI()


# Dépendance pour la session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)
