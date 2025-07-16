import os

import pandas as pd
from fastapi import APIRouter, FastAPI

from database.schemas.user_schema import UserIn

from .model_loader import load_model_and_preprocessor

# Disable GPU usage (force CPU)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Initialize FastAPI app
app = FastAPI()

# Create API router
router = APIRouter()

# Load trained model and preprocessor
model, preprocessor = load_model_and_preprocessor()


@router.post("/predict_income")
def predict_income(user: UserIn):
    # Convert input to DataFrame
    input_df = pd.DataFrame([user.dict()])

    # Preprocess input
    X = preprocessor.transform(input_df)

    # Make prediction
    prediction = model.predict(X)
    predicted_income = ">50K" if prediction[0] == 1 else "<=50K"

    return {"predicted_income": predicted_income}


# Register router with app
app.include_router(router)
