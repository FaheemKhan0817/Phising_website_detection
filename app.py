import streamlit as st
import joblib
import pandas as pd

# Load model & scaler
model = joblib.load("best_phishing_model.pkl")
scaler = joblib.load("best_scaler.pkl")

st.set_page_config(page_title="Phishing Website Detector", page_icon="🔎", layout="centered")

# Header
st.title("🔎 Phishing Website Detection")
st.markdown("This ML app classifies websites as **Legitimate** or **Phishing** using the top 15 most important features identified by Random Forest.")

# Features
features = [
    'SSLfinal_State', 'URL_of_Anchor', 'Prefix_Suffix', 'web_traffic',
    'having_Sub_Domain', 'age_of_domain', 'Page_Rank', 'Links_in_tags',
    'Domain_registeration_length', 'Request_URL', 'Links_pointing_to_page',
    'DNSRecord', 'Google_Index', 'URL_Length', 'SFH'
]

st.subheader("📝 Enter Website Features")

cols = st.columns(2)
user_input = []

for i, feat in enumerate(features):
    with cols[i % 2]:
        val = st.number_input(f"{feat}", value=0, step=1)
        user_input.append(val)

# --- Prediction Function ---
def make_prediction(input_data):
    input_df = pd.DataFrame([input_data], columns=features)
    data_scaled = scaler.transform(input_df)
    pred = model.predict(data_scaled)[0]
    prob = model.predict_proba(data_scaled)[0][1]
    return pred, prob

# Prediction button
if st.button("🚀 Predict"):
    pred, prob = make_prediction(user_input)
    label = "Phishing" if pred == 1 else "Legitimate"
    emoji = "⚠️" if label == "Phishing" else "✅"

    st.markdown("---")
    st.subheader("📊 Prediction Result")
    st.success(f"{emoji} **Predicted Label:** {label}")
    st.info(f"🔒 Phishing Probability: **{round(prob, 3)}**")
    st.progress(int(prob * 100))

# --- Demo Button ---
if st.button("🎯 Try Demo Data"):
    demo = [1, -1, 1, 2, 1, 0, 3, 1, 2, 1, 1, 2, 1, 45, -1]  # Example demo row
    pred, prob = make_prediction(demo)
    label = "Phishing" if pred == 1 else "Legitimate"
    emoji = "⚠️" if label == "Phishing" else "✅"

    st.markdown("---")
    st.subheader("📊 Demo Prediction Result")
    st.success(f"{emoji} **Predicted Label:** {label}")
    st.info(f"🔒 Phishing Probability: **{round(prob, 3)}**")
    st.progress(int(prob * 100))
