import joblib
from tensorflow import keras


def load_model_and_preprocessor():
    model = keras.models.load_model("model_artifacts/model1.keras")
    preprocessor = joblib.load("model_artifacts/preprocessor2.pkl")
    return model, preprocessor
