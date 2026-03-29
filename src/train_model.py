import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def train_model(data_path="data/fea_dataset.csv", model_path="models/random_forest.pkl"):
    df = pd.read_csv(data_path)

    X = df[['Load', 'Moment']]
    y = df[['Deformation', 'Equivalent_Stress', 'Max_Principal_Stress', 'Shear_Stress']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(
    n_estimators=500,
    max_depth=12,
    min_samples_split=4,
    min_samples_leaf=2,
    random_state=42
    )
    model.fit(X_train, y_train)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print("Model trained and saved!")

    return X_test, y_test, model

if __name__ == "__main__":
    train_model()