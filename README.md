# 💳 Credit Card Fraud Detection

A Machine Learning project that detects fraudulent credit card transactions using **Logistic Regression** and a **Streamlit web application**.



## 📌 Project Overview

Credit card fraud is a major issue in the financial industry. This project uses machine learning to classify transactions as:

* **0 → Genuine Transaction**
* **1 → Fraudulent Transaction**

The model is trained on a highly imbalanced dataset and uses data balancing and feature scaling to improve fraud detection performance.



## 🚀 Features

* Detect fraudulent transactions
* Logistic Regression model
* Data balancing for better performance
* StandardScaler for feature normalization
* Streamlit web application
* Saved model using Pickle
* User-friendly interface

---

## 📂 Dataset

Dataset contains:

* **Time**
* **V1 – V28** (PCA transformed features)
* **Amount**
* **Class**

  * 0 = Genuine Transaction
  * 1 = Fraudulent Transaction

> Note: V1-V28 are PCA-transformed features used to protect customer privacy.

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Pickle

---

## 🤖 Machine Learning Model

**Algorithm Used:**

* Logistic Regression

**Preprocessing:**

* Train-Test Split
* Data Scaling using StandardScaler
* Handling Imbalanced Dataset

---

## 📊 Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 93%   |
| Precision | 98%   |
| Recall    | 88%   |
| F1 Score  | 92%   |

---

## 📁 Project Structure

```text
credit-card-fraud-detection/
│
├── app.py
├── fraud_model.pkl
├── scaler.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/RakshithaReddy28/credit-card-fraud-detection.git
```

Move into the project directory:

```bash
cd credit-card-fraud-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

streamlit run app.py

Open the browser:

http://localhost:8501

## 📈 Future Improvements

* Random Forest and XGBoost models
* CSV file upload support
* Batch prediction
* Interactive dashboard
* Deployment using Streamlit Cloud


## 👩‍💻 Author

**Rakshitha Reddy**

GitHub:
https://github.com/RakshithaReddy28

---

⭐ If you found this project useful, please consider giving it a star!
