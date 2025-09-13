import streamlit as st
import numpy as np
import joblib

# Load saved model and scaler
model = joblib.load("best_phishing_model.pkl")
scaler = joblib.load("best_scaler.pkl")

# Top 15 Features (Model-Based)
top_features = [
    'SSLfinal_State', 'URL_of_Anchor', 'web_traffic', 'Prefix_Suffix',
    'having_Sub_Domain', 'age_of_domain', 'Page_Rank', 'Links_in_tags',
    'Domain_registeration_length', 'Request_URL', 'Links_pointing_to_page',
    'DNSRecord', 'Google_Index', 'URL_Length', 'HTTPS_token'
]

# Streamlit Page Config
st.set_page_config(page_title="Phishing Detector", page_icon="🛡️", layout="centered")

# Custom CSS for better look
st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    .result-box {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
        font-size: 18px;
        font-weight: bold;
    }
    .legit {
        background-color: #e6f9f0;
        color: #2e7d32;
        border: 2px solid #2e7d32;
    }
    .phish {
        background-color: #fdecea;
        color: #c62828;
        border: 2px solid #c62828;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>🛡️ Phishing Website Detector</h1>", unsafe_allow_html=True)
st.write("Fill in the feature values below to check if a website is **Phishing** or **Legitimate**.")

# Input Form
with st.form("feature_form"):
    st.subheader("✏️ Enter Website Features")
    
    user_input = []
    cols = st.columns(2)  # Two columns layout
    for i, feature in enumerate(top_features):
        with cols[i % 2]:
            value = st.number_input(f"{feature}:", value=0.0, format="%.5f")
            user_input.append(value)

    submit_button = st.form_submit_button("🔍 Predict")

# Prediction
if submit_button:
    features_array = np.array(user_input).reshape(1, -1)
    features_scaled = scaler.transform(features_array)

    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]

    st.subheader("🔎 Prediction Result")
    if prediction == 1:
        st.markdown(f"<div class='result-box phish'>⚠️ The website is <b>Phishing</b><br>Confidence: {probability:.2%}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='result-box legit'>✅ The website is <b>Legitimate</b><br>Confidence: {1 - probability:.2%}</div>", unsafe_allow_html=True)

    st.write("📊 Confidence Level")
    st.progress(float(probability))
