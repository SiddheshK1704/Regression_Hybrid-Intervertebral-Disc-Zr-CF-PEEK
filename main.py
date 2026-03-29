from src.generate_data import generate_dataset
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.visualize import plot_results
from src.predict import predict_values
from src.eda import perform_eda

def main():
    # Step 1
    generate_dataset()
    perform_eda() 

    # Step 2
    X_test, y_test, model = train_model()

    # Step 3
    y_pred = evaluate_model(X_test, y_test, model)

    # Step 4
    plot_results(
        y_test,
        y_pred,
        ['Deformation', 'Equivalent_Stress', 'Max_Principal_Stress', 'Shear_Stress']
    )

    # Step 5 (Demo prediction)
    print("\n🔹 Demo Prediction 🔹")
    result = predict_values(1000, 10)

    for k, v in result.items():
        print(f"{k}: {v:.3f}")


if __name__ == "__main__":
    main()