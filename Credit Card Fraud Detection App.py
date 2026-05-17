import streamlit as st
import numpy as np
import joblib as jb

# Load model and scaler
model = jb.load("fraud_detection_model.joblib")
scaler = jb.load("scaler.joblib")
features = jb.load("feature_names.joblib")

st.title("Credit Card Fraud Detection App")

st.write("Enter transaction details below:")

# Example inputs
time = st.number_input("Transaction Time")
amount = st.number_input("Transaction Amount")

V1 = st.number_input("V1")
V2 = st.number_input("V2")
V3 = st.number_input("V3")
V4 = st.number_input("V4")
V5 = st.number_input("V5")
V6 = st.number_input("V6")
V7 = st.number_input("V7")
V8 = st.number_input("V8")
V9 = st.number_input("V9")
V10 = st.number_input("V10")
V11 = st.number_input("V11")
V12 = st.number_input("V12")
V13 = st.number_input("V13")
V14 = st.number_input("V14")
V15 = st.number_input("V15")
V16 = st.number_input("V16")
V17 = st.number_input("V17")
V18 = st.number_input("V18")
V19 = st.number_input("V19")
V20 = st.number_input("V20")
V21 = st.number_input("V21")
V22 = st.number_input("V22")
V23 = st.number_input("V23")
V24 = st.number_input("V24")
V25 = st.number_input("V25")
V26 = st.number_input("V26")
V27 = st.number_input("V27")
V28 = st.number_input("V28")


# Add remaining features as needed...

if st.button("Check Transaction"):
    features = np.array([[time, V1, V2, V3, V5, V6, V7, V23, V24, V25, V26, V27, V28, amount]])
    
    st.write("Scaler expects:", scaler.n_features_in_)
    st.write("Features provided:", features.shape[1])
    
    # Scale features
    scaled_features = scaler.transform(features)
    
    # Predict
    prediction = model.predict(scaled_features)
    
    if prediction[0] == 1:
        st.error("Fraudulent Transaction Detected!")
    else:
        st.success("Legitimate Transaction")

