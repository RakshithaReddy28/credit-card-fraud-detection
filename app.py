import streamlit as st
import pickle
import numpy as np

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# ---------------- Load Model ----------------
model = pickle.load(open("fraud_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ---------------- Sidebar ----------------
st.sidebar.title("ℹ About this Application")

st.sidebar.info("""
### Credit Card Fraud Detection

This application predicts whether a transaction is:

✅ Genuine Transaction

🚨 Fraudulent Transaction

**Model Used:** Logistic Regression

**Dataset Features:**

• Time

• V1 - V28 (PCA-transformed anonymized features)

• Amount

**Note:**
V1-V28 are anonymized features created using PCA to protect customer privacy. Their original meanings are unknown.
""")

# ---------------- Title ----------------
st.title("💳 Credit Card Fraud Detection System")

st.markdown("""
Detect whether a credit card transaction is **Genuine** or **Fraudulent**.

### Instructions
1. Enter transaction details below.
2. V1-V28 are anonymized PCA features.
3. Click **Predict Transaction**.
""")

st.markdown("---")

# ---------------- Input Section ----------------
st.subheader("Transaction Details")

col1, col2, col3 = st.columns(3)

with col1:
    time = st.number_input("⏰ Time")

    v1 = st.number_input("Feature V1 (Anonymized)")
    v2 = st.number_input("Feature V2 (Anonymized)")
    v3 = st.number_input("Feature V3 (Anonymized)")
    v4 = st.number_input("Feature V4 (Anonymized)")
    v5 = st.number_input("Feature V5 (Anonymized)")
    v6 = st.number_input("Feature V6 (Anonymized)")
    v7 = st.number_input("Feature V7 (Anonymized)")
    v8 = st.number_input("Feature V8 (Anonymized)")
    v9 = st.number_input("Feature V9 (Anonymized)")

with col2:

    v10 = st.number_input("Feature V10 (Anonymized)")
    v11 = st.number_input("Feature V11 (Anonymized)")
    v12 = st.number_input("Feature V12 (Anonymized)")
    v13 = st.number_input("Feature V13 (Anonymized)")
    v14 = st.number_input("Feature V14 (Anonymized)")
    v15 = st.number_input("Feature V15 (Anonymized)")
    v16 = st.number_input("Feature V16 (Anonymized)")
    v17 = st.number_input("Feature V17 (Anonymized)")
    v18 = st.number_input("Feature V18 (Anonymized)")
    v19 = st.number_input("Feature V19 (Anonymized)")

with col3:

    v20 = st.number_input("Feature V20 (Anonymized)")
    v21 = st.number_input("Feature V21 (Anonymized)")
    v22 = st.number_input("Feature V22 (Anonymized)")
    v23 = st.number_input("Feature V23 (Anonymized)")
    v24 = st.number_input("Feature V24 (Anonymized)")
    v25 = st.number_input("Feature V25 (Anonymized)")
    v26 = st.number_input("Feature V26 (Anonymized)")
    v27 = st.number_input("Feature V27 (Anonymized)")
    v28 = st.number_input("Feature V28 (Anonymized)")

    amount = st.number_input("💰 Transaction Amount")

st.markdown("---")

# ---------------- Prediction ----------------
if st.button("🚀 Predict Transaction"):

    input_data = np.array([[
        time,
        v1, v2, v3, v4, v5, v6, v7,
        v8, v9, v10, v11, v12, v13,
        v14, v15, v16, v17, v18, v19,
        v20, v21, v22, v23, v24, v25,
        v26, v27, v28,
        amount
    ]])

    # Scale Input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    st.markdown("---")

    st.subheader("Prediction Result")

    if prediction[0] == 0:
        st.success("✅ Genuine Transaction")
        st.balloons()

    else:
        st.error("🚨 Fraudulent Transaction")

# ---------------- Footer ----------------
st.markdown("---")

st.caption("💻 Developed by Rakshitha Reddy ❤️")

