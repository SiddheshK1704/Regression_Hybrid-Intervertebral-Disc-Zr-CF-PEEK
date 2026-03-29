import numpy as np
import pandas as pd
import os

def generate_dataset(n_samples=400, save_path="data/fea_dataset.csv"):
    np.random.seed(42)

    # Input ranges
    load = np.random.uniform(500, 2000, n_samples)
    moment = np.random.uniform(6, 10, n_samples)

    # Normalize inputs (for smooth interpolation)
    load_norm = (load - 500) / (2000 - 500)
    moment_norm = (moment - 6) / (10 - 6)

    # -------------------------------
    # Outputs (INTERPOLATED + NOISE)
    # -------------------------------

    # Deformation (0.25 → 1.02)
    deformation = (
        0.25 + 0.75 * load_norm + 0.05 * moment_norm
    ) + np.random.normal(0, 0.015, n_samples)

    # Equivalent Stress (22 → 92)
    eq_stress = (
        22 + 70 * load_norm + 3 * moment_norm
    ) + np.random.normal(0, 2, n_samples)

    # Max Principal Stress (12.5 → 49)
    max_principal = (
        12.5 + 36 * load_norm + 2 * moment_norm
    ) + np.random.normal(0, 1.5, n_samples)

    # Shear Stress (4 → 18)
    shear_stress = (
        4 + 12 * load_norm + 3 * moment_norm
    ) + np.random.normal(0, 1, n_samples)

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

    print("✅ Dataset generated using real FEA anchor interpolation")

if __name__ == "__main__":
    generate_dataset()