import matplotlib.pyplot as plt
import os

def plot_results(y_test, y_pred, feature_names, save_dir="outputs/plots"):
    os.makedirs(save_dir, exist_ok=True)

    for i, col in enumerate(feature_names):
        plt.figure()
        plt.scatter(y_test[col], y_pred[:, i])
        plt.xlabel("Actual")
        plt.ylabel("Predicted")
        plt.title(f"{col}: Actual vs Predicted")

        plt.savefig(f"{save_dir}/{col}.png")
        plt.close()

    print("Plots saved!")