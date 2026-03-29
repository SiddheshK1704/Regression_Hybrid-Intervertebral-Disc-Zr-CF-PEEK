import pickle
import numpy as np

MODEL_PATH = "models/random_forest.pkl"

def load_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

def predict_values(load, moment):
    model = load_model()

    # Input must be 2D
    input_data = np.array([[load, moment]])

    prediction = model.predict(input_data)[0]

    result = {
        "Deformation (mm)": prediction[0],
        "Equivalent Stress (MPa)": prediction[1],
        "Max Principal Stress (MPa)": prediction[2],
        "Shear Stress (MPa)": prediction[3],
    }

    return result


if __name__ == "__main__":
    print("\n🔹 Enter Input Values 🔹")
    load = float(input("Enter Load (N): "))
    moment = float(input("Enter Moment (Nm): "))

    result = predict_values(load, moment)

    print("\n📊 Predicted Results:")
    for key, value in result.items():
        print(f"{key}: {value:.3f}")