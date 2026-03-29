import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(X_test, y_test, model, output_path="outputs/metrics.txt"):
    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    with open(output_path, "w") as f:
        f.write(f"R2 Score: {r2}\n")
        f.write(f"MSE: {mse}\n")

    print("Evaluation done. Metrics saved.")

    return y_pred