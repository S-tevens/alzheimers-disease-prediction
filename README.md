# 🧠 Alzheimer’s Disease Prediction

This project uses machine learning to classify early-stage Alzheimer’s Disease using clinical data from the [OASIS dataset](https://www.oasis-brains.org/). It aims to assist in early diagnosis through features such as age, brain volume, and cognitive scores.

## 📊 Problem Statement

Alzheimer’s is a progressive neurological disorder, and early detection is crucial for treatment and management. This project builds a classification model to predict early-stage Alzheimer’s using medical and cognitive data.

---

## 🧪 Dataset

- **Source**: OASIS-1 dataset
- **Features Used**:
  - Age
  - MRI-measured brain volumes (e.g., eTIV, nWBV)
  - Cognitive test scores (MMSE, CDR)
  - Gender, Education level

---

## 🧰 Tech Stack

- **Programming Language**: Python
- **Libraries**:  
  - `Pandas`, `NumPy` – data handling  
  - `Scikit-learn` – preprocessing, modeling, evaluation  
  - `XGBoost` – high-performance gradient boosting  
  - `Matplotlib`, `Seaborn` – visualization

---

## 🔍 Exploratory Data Analysis

- Visualized distribution of cognitive scores and brain volume by diagnosis category
- Detected and handled missing values
- Normalized feature scales for fair comparison
- Performed correlation analysis and feature importance

---

## 🤖 Model Building

- Compared several classifiers: Logistic Regression, Random Forest, XGBoost
- Evaluated using:
  - Accuracy, Precision, Recall, F1-score
  - ROC-AUC curve
- XGBoost achieved the best results with high recall on early-stage patients

---

## 📈 Results

| Model              | Accuracy | Precision | Recall | F1-score |
|-------------------|----------|-----------|--------|----------|
| Logistic Regression | 82%     | 79%       | 81%    | 80%      |
| XGBoost             | **89%** | **86%**   | **88%**| **87%**  |

---

## 📌 Key Insights

- Age and MMSE (Mini-Mental State Examination) score were the most predictive features
- Brain volume and cognitive scores show strong correlations with early-stage detection

---

## 🚀 Future Improvements

- Include time-series analysis to track cognitive decline over time
- Integrate with a clinical decision support system (CDSS) for practical use

---

## 📁 Project Structure

