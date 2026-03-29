from src.generate_data import generate_dataset
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.visualize import plot_results

def main():
    # Step 1: Generate dataset
    generate_dataset()

    # Step 2: Train model
    X_test, y_test, model = train_model()

    # Step 3: Evaluate
    y_pred = evaluate_model(X_test, y_test, model)

    # Step 4: Visualize
    plot_results(
        y_test,
        y_pred,
        ['Deformation', 'Equivalent_Stress', 'Max_Principal_Stress', 'Shear_Stress']
    )

if __name__ == "__main__":
    main()