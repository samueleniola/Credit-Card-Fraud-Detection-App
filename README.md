# Credit-Card-Fraud-Detection-App

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)

A machine learning system for detecting fraudulent credit card transactions using ensemble methods and anomaly detection techniques. The dataset contains **284,807 transactions** with **31 features**, where only **0.17% are fraudulent**.

## 📊 Dataset Overview

- **Source**: European cardholders (September 2013)
- **Transactions**: 284,807
- **Features**: 31 (28 PCA-transformed + Time + Amount + Class)
- **Fraud Rate**: 0.172% (492 fraudulent transactions)
- **Challenge**: Extreme class imbalance

### Feature Description
| Feature | Description |
|---------|-------------|
| V1-V28  | PCA-transformed features (confidential) |
| Time    | Seconds elapsed between transactions |
| Amount  | Transaction amount |
| Class   | 0 = Legitimate, 1 = Fraudulent |

## 🎯 Project Objectives

1. **Detect fraudulent transactions** with high recall (>95%)
2. **Minimize false positives** to avoid blocking legitimate customers
3. **Handle extreme class imbalance** (1:577 ratio)
4. **Provide interpretable results** for business stakeholders
5. **Create production-ready pipeline** for real-time scoring

## 🛠️ Tech Stack

### Core Libraries
- **Data Processing**: Pandas, NumPy, SciPy
- **Machine Learning**: Scikit-learn, Imbalanced-learn
- **Modeling**: XGBoost, LightGBM, Logistic Regression, Gradient Boosting
- **Visualization**: Matplotlib, Seaborn, SHAP
- **Model Explanation**: SHAP, Feature Importance
- **Serialization**: Joblib, Pickle

### Development Tools
- Jupyter Notebooks & Google Colab for experimentation
- Git for version control
- Virtual environment for dependency management
