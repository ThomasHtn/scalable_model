import os
import sys

from sqlalchemy.orm import Session

from database.models.user_model import User

# Add folder parent in PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def get_all_users(db: Session):
    return db.query(User).all()
