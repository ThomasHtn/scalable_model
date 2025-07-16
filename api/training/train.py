import os
import sys

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
import requests
from sklearn.model_selection import train_test_split

from .evaluate import draw_loss, draw_loss_mlflow, evaluate_performance, print_data
from .model import create_nn_model, model_predict
from .preprocess import preprocessing

# Add folder parent in PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def fetch_data_from_api():
    response = requests.get("http://localhost:8000/users/")
    response.raise_for_status()
    return pd.DataFrame(response.json())


def train_model(
    model, X, y, X_val=None, y_val=None, epochs=50, batch_size=32, verbose=0
):
    hist = model.fit(
        X,
        y,
        validation_data=(X_val, y_val)
        if X_val is not None and y_val is not None
        else None,
        epochs=epochs,
        batch_size=batch_size,
        verbose=verbose,
    )
    return model, hist


def split(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    return X_train, X_test, y_train, y_test


def simple_model_train(numerical_cols, categorical_cols, predict_col):
    # Load data from database
    df = fetch_data_from_api()

    # 🔁 Encodage binaire de la colonne cible
    df[predict_col] = df[predict_col].apply(lambda x: 1 if x.strip() == ">50K" else 0)

    # Séparation X / y
    y = df[predict_col]
    df = df.drop(columns=[predict_col, "id"])

    # Preprocessing data
    X, _, preprocessor = preprocessing(df, numerical_cols, categorical_cols)

    # split data in train and test dataset
    X_train, X_test, y_train, y_test = split(X, y)

    # create a new model
    model = create_nn_model(X_train.shape[1])

    # First model train
    model, hist = train_model(model, X_train, y_train, X_val=X_test, y_val=y_test)
    y_pred = model_predict(model, X_test)
    perf = evaluate_performance(y_test, y_pred)
    print_data(perf, "Performance after training")

    # display val loss graph
    draw_loss(hist)

    # Save model
    model.save(os.path.join("model_artifacts", "model1.keras"))
    joblib.dump(preprocessor, os.path.join("model_artifacts", "preprocessor2.pkl"))
    print("Model and preprocessor saved.")

    # Log dans MLflow
    mlflow.set_experiment("my_experiment")
    with mlflow.start_run(run_name="Train - less columns"):
        mlflow.log_metric("mse", perf["MSE"])
        mlflow.log_metric("mae", perf["MAE"])
        mlflow.log_metric("r2", perf["R²"])
        draw_loss_mlflow(hist, mlflow)
        mlflow.sklearn.log_model(model, artifact_path="model")
