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

## Key Insights — Credit Card Fraud Detection App

# 1. Extreme Class Imbalance

One of the biggest insights from this project is that fraud detection datasets are highly imbalanced.
	•	Total transactions: 284,807
	•	Fraudulent transactions: 492
	•	Fraud rate: 0.172%

# 2. Accuracy Alone is Misleading

A model can achieve over 99% accuracy and still fail to detect fraud properly because fraud cases are extremely rare.

Important evaluation metrics include:
	•	Precision
	•	Recall
	•	F1-score
	•	ROC-AUC

# 3.Anomaly Detection is Effective

Fraudulent transactions behave differently from normal spending patterns.

The project uses:
	•	Anomaly Detection
	•	Ensemble Learning

 # 4. PCA-Transformed Features Improve Privacy

Features V1–V28 are PCA-transformed.

Key insight:
	•	Sensitive customer information is hidden
	•	Data privacy is preserved
	•	Models still learn transaction behavior patterns effectively

# 5. Ensemble Models Improve Detection

Combining multiple models generally performs better than using a single algorithm.

ML models:
	•	Random Forest
	•	XGBoost
	•	Logistic Regression
	•	LGBM

Ensemble methods improve:
	•	Stability
	•	Generalization
	•	Fraud detection capability

# 6. Real-Time Fraud Detection is Possible

This project demonstrates how machine learning can:
	•	Monitor transactions in real time
	•	Flag suspicious activities instantly
	•	Reduce manual review workload

This is how modern banking systems operate.

# 7. Feature Engineering Matters

Features like:
	•	Transaction amount
	•	Time patterns
	•	Behavioral anomalies

can significantly influence fraud prediction performance.

Understanding transaction behavior is often more important than model complexity alone.

# 8. Business Impact

A successful fraud detection system:
	•	Prevent financial losses
	•	Increase customer trust
	•	Reduce chargebacks
	•	Improve banking security
	•	Automate fraud monitoring

 # 9.End-to-End ML Engineering Skills Demonstrated

This project showcases:
	•	Data preprocessing
	•	Handling imbalanced datasets
	•	Model training
	•	Model evaluation
	•	Deployment readiness
	•	API/Application integration
