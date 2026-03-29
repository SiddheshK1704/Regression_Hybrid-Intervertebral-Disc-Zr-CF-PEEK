import pandas as pd
import matplotlib.pyplot as plt
import os

def perform_eda(data_path="data/fea_dataset.csv", save_dir="outputs/eda"):
    df = pd.read_csv(data_path)

    os.makedirs(save_dir, exist_ok=True)

    # -----------------------------
    # 1. HISTOGRAMS
    # -----------------------------
    df.hist(figsize=(12, 8))
    plt.suptitle("Feature Distributions")
    plt.savefig(f"{save_dir}/histograms.png")
    plt.close()

    # -----------------------------
    # 2. SCATTER: Load vs Outputs
    # -----------------------------
    for col in df.columns[2:]:
        plt.figure()
        plt.scatter(df['Load'], df[col])
        plt.xlabel("Load (N)")
        plt.ylabel(col)
        plt.title(f"Load vs {col}")
        plt.savefig(f"{save_dir}/load_vs_{col}.png")
        plt.close()

    # -----------------------------
    # 3. SCATTER: Moment vs Outputs
    # -----------------------------
    for col in df.columns[2:]:
        plt.figure()
        plt.scatter(df['Moment'], df[col])
        plt.xlabel("Moment (Nm)")
        plt.ylabel(col)
        plt.title(f"Moment vs {col}")
        plt.savefig(f"{save_dir}/moment_vs_{col}.png")
        plt.close()

    # -----------------------------
    # 4. CORRELATION HEATMAP
    # -----------------------------
    corr = df.corr()

    plt.figure(figsize=(8, 6))
    plt.imshow(corr)
    plt.colorbar()

    plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
    plt.yticks(range(len(corr.columns)), corr.columns)

    plt.title("Correlation Matrix")
    plt.savefig(f"{save_dir}/correlation_matrix.png")
    plt.close()

    print("✅ EDA plots saved in outputs/eda/")


if __name__ == "__main__":
    perform_eda()