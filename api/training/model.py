from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential


def create_nn_model(input_dim):
    """
    Fonction pour créer et compiler un modèle de réseau de neurones simple.
    """
    model = Sequential()
    model.add(Dense(12, activation="relu", input_dim=input_dim))
    model.add(Dense(6, activation="relu"))
    model.add(Dense(1))
    model.compile(optimizer="adam", loss="mse")
    return model


def model_predict(model, X):
    y_pred = model.predict(X).flatten()
    return y_pred
