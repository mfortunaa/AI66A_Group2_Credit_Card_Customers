# 🏦 Bank Customer Churn Prediction

## Project Overview
Customer attrition (churn) is one of the biggest expenditures for any organization. In the banking sector, it is significantly cheaper to retain existing customers than to acquire new ones. 

This project aims to build a robust Machine Learning pipeline to predict whether a credit card customer will leave the bank (attrited customer) or stay (existing customer). By identifying customers at high risk of churning, the bank can proactively offer better services, targeted promotions, and retain their business.

## Objectives
* **Technical:** Develop a highly accurate Binary Classification model, specifically focusing on maximizing **Recall** for the minority class (Churners) without sacrificing too much Precision.
* **Business:** Identify the root causes and key indicators of customer churn using advanced model interpretability tools to assist the CRM and Marketing teams in making data-driven retention strategies.

## Dataset
* **Source:** [Credit Card Customers Dataset on Kaggle](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers)
* **Description:** The dataset consists of 10,127 customers with 21 features encompassing demographic information (Age, Education, Income) and banking behavior (Transaction Amount, Revolving Balance, Inactive Months).
* **Note:** The dataset is highly imbalanced, with only ~16% of customers having churned. The original dataset contains some Naive Bayes reference columns that were excluded during preprocessing to prevent data leakage.

## Tech Stack
* **Language:** Python
* **Data Manipulation & Analysis:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn, SHAP (SHapley Additive exPlanations)
* **Machine Learning:** Scikit-Learn, LightGBM, XGBoost, CatBoost
* **Hyperparameter Tuning:** Optuna
* **Imbalanced Data Handling:** Imbalanced-learn (SMOTE)

## Project Workflow
The project is structured into sequential Jupyter Notebooks:
1. **`01_EDA.ipynb`:** Exploratory Data Analysis to uncover hidden patterns and understand the distribution of customer attributes.
2. **`02_Preprocessing.ipynb`:** Data cleaning, feature engineering (e.g., creating `Avg_Amt_Per_Trans`), encoding categorical variables, and scaling.
3. **`03_Modeling.ipynb`:** Training baseline models (Logistic Regression, Random Forest, LightGBM, etc.) using Strict 5-Fold Cross-Validation.
4. **`04_Advanced_Tuning_and_Stacking.ipynb`:** * Tuning base models (LightGBM, XGBoost, CatBoost) using **Optuna**.
   * Building a **Stacking Ensemble** with Logistic Regression as the Meta-model.
   * Optimizing the decision threshold to prioritize Recall.
   * Extracting business insights using **SHAP** Force and Waterfall plots.

## Key Findings & Results
* **Model Performance:** The project successfully evolved from a strong LightGBM Baseline (F1-Score: ~0.9068) to a highly optimized **Stacking Ensemble Classifier**, successfully pushing the model's ability to catch true churners to its absolute limit.
* **Threshold Optimization:** By lowering the decision threshold from the default 0.5, we strategically prioritized Recall (catching more churners), aligning with the business logic that false alarms are cheaper than losing a customer.
* **Top Drivers of Churn:** SHAP analysis revealed the top 3 warning signs of a churning customer:
  1. **Total_Trans_Amt:** Sudden drops in transaction volume.
  2. **Total_Revolving_Bal:** Low credit limit utilization.
  3. **Total_Ct_Chng_Q4_Q1 & Months_Inactive_12_mon:** Decreased engagement and prolonged inactivity.

## How to Run
1. Clone this repository to your local machine.
2. Ensure you have Python 3.8+ installed.
3. Install the required dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn lightgbm xgboost catboost optuna imbalanced-learn shap