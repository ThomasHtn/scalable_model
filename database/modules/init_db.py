import pandas as pd
from sqlalchemy.orm import Session

from database.database import Base, SessionLocal, engine
from database.models.user_model import User


def load_csv_to_db(csv_path: str):
    df = pd.read_csv(
        csv_path,
        names=[
            "age",
            "workclass",
            "fnlwgt",
            "education",
            "education_num",
            "marital_status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "capital_gain",
            "capital_loss",
            "hours_per_week",
            "native_country",
            "income",
        ],
        skipinitialspace=True,
    )

    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()
    try:
        for _, row in df.iterrows():
            user = User(**row.to_dict())
            db.add(user)
        db.commit()
    finally:
        db.close()


if __name__ == "__main__":
    load_csv_to_db("data/raw/adult.data")
