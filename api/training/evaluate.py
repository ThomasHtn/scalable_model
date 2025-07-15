import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate_performance(y_true, y_pred):
    """
    Fonction pour mesurer les performances du modèle avec MSE, MAE et R².
    """
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {"MSE": mse, "MAE": mae, "R²": r2}


def print_data(dico, exp_name):
    mse = dico["MSE"]
    mae = dico["MAE"]
    r2 = dico["R²"]

    print(f"{exp_name:^60}".replace(" ", "="))
    print(f"MSE: {mse:.4f}, MAE: {mae:.4f}, R²: {r2:.4f}")
    print("=" * 60)


def draw_loss(history):
    """
    Affiche les courbes de loss et val_loss de l'historique d'entraînement.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(history.history["loss"], label="Loss (Entraînement)")
    plt.plot(history.history["val_loss"], label="Val Loss (Validation)", linestyle="--")
    plt.title("Courbes de Loss et Val Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True)
    plt.show()


def draw_loss_mlflow(history, mlflow):
    """
    Display loss and val_loss in mlflow.
    """

    plt.figure(figsize=(10, 5))
    plt.plot(history.history["loss"], label="Train Loss")
    if "val_loss" in history.history:
        plt.plot(history.history["val_loss"], label="Validation Loss")
    plt.title("Courbe de perte")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()

    mlflow.log_figure(plt.gcf(), "loss_curve.png")
    plt.close()
