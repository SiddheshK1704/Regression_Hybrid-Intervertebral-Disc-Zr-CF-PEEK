import numpy as np
import pandas as pd
import os

def generate_dataset(n_samples=300, save_path="data/fea_dataset.csv"):
    np.random.seed(42)

    load = np.random.uniform(200, 2000, n_samples)
    moment = np.random.uniform(1, 20, n_samples)

    deformation = (0.0005 * load + 0.02 * moment) + np.random.normal(0, 0.02, n_samples)
    eq_stress = (0.08 * load + 2.5 * moment) + np.random.normal(0, 5, n_samples)
    max_principal = (0.09 * load + 2.8 * moment) + np.random.normal(0, 5, n_samples)
    shear_stress = (0.03 * load + 4.5 * moment) + np.random.normal(0, 3, n_samples)

    df = pd.DataFrame({
        'Load': load,
        'Moment': moment,
        'Deformation': deformation,
        'Equivalent_Stress': eq_stress,
        'Max_Principal_Stress': max_principal,
        'Shear_Stress': shear_stress
    })

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"Dataset saved at {save_path}")

if __name__ == "__main__":
    generate_dataset()