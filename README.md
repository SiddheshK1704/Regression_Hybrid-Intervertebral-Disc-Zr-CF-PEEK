# 🧠 AI-Based Surrogate Modeling of Hybrid Intervertebral Disc

## 📌 Overview
This project focuses on developing an AI-based surrogate model for predicting biomechanical responses of a hybrid artificial intervertebral disc composed of:

- PEEK (Polyether ether ketone)
- Carbon Fiber (CF)
- Zirconium + 1% Ag core

Instead of running computationally expensive Finite Element Analysis (FEA) repeatedly, this project uses a **Random Forest Regression model** to approximate results based on loading conditions.

---

## 🎯 Objective
To predict the following biomechanical parameters using machine learning:

- Total Deformation (mm)
- Equivalent Stress (MPa)
- Maximum Principal Stress (MPa)
- Shear Stress (MPa)

### Inputs:
- Load (N)
- Moment (Nm)

---

## 🧱 System Architecture
FEA-Inspired Data → Dataset Generation → Random Forest Model → Prediction → Visualization

---

## 📁 Project Structure

```
fea_ai_project/
│
├── data/
│ └── fea_dataset.csv
│
├── src/
│ ├── generate_data.py
│ ├── train_model.py
│ ├── evaluate_model.py
│ └── visualize.py
│
├── models/
│ └── random_forest.pkl
│
├── outputs/
│ ├── plots/
│ └── metrics.txt
│
├── requirements.txt
└── main.py
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/fea-ai-disc-model.git
cd fea-ai-disc-model

```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the full pipeline:
```
python main.py
```
This will:

Generate synthetic dataset
Train Random Forest model
Evaluate performance
Save plots and metrics

---

## 📊 Dataset Details

The dataset is synthetically generated using engineering-informed relationships:

Deformation increases with load and moment
Equivalent stress is primarily influenced by load
Shear stress is more dependent on moment

Noise is added to simulate real-world FEA variations.

---


## 🌲 Machine Learning Model
Algorithm: Random Forest Regressor
Type: Multi-output regression
Features:
Handles nonlinear relationships
Robust to noise
Requires minimal tuning

---

## 📈 Outputs
Metrics:
R² Score
Mean Squared Error (MSE)
Visualizations:
Actual vs Predicted plots for all outputs
Feature importance analysis

---

## 🧠 Key Concept: Surrogate Modeling

This project demonstrates surrogate modeling, where:

A machine learning model approximates the behavior of a computationally expensive simulation (FEA).

Advantages:
Faster predictions
Reduced computational cost
Enables optimization workflows

---

## 🚀 Future Work
Integrate real FEA simulation data
Hyperparameter tuning
Add optimization algorithms (Genetic Algorithm / Bayesian Optimization)
Deploy as a web app or GUI tool
Expand inputs (material properties, geometry variations)

---

## 📚 Applications
Biomedical implant design
Spine biomechanics research
Simulation acceleration
AI-driven engineering optimization

---


## ⚠️ Disclaimer

This dataset is synthetically generated and does not replace actual FEA simulations. It is intended for academic and demonstration purposes only.

---

##👨‍💻 Author
Siddhesh Khankhoje
