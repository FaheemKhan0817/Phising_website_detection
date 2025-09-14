# phishing_app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load model and scaler
# -----------------------------
best_model = joblib.load("best_phishing_model.pkl")
scaler_model = joblib.load("best_scaler.pkl")

# List of features used in the model (top 15 model-based features)
top_features_model_based = [
    'SSLfinal_State', 'URL_of_Anchor', 'web_traffic', 'Prefix_Suffix', 
    'having_Sub_Domain', 'age_of_domain', 'Page_Rank', 'Links_in_tags', 
    'Domain_registeration_length', 'Request_URL', 'Links_pointing_to_page', 
    'DNSRecord', 'Google_Index', 'URL_Length', 'HTTPS_token'
]

# -----------------------------
# Safe Prediction Function
# -----------------------------
def predict_phishing_safe(input_features, model, scaler, feature_names):
    if isinstance(input_features, list) or isinstance(input_features, np.ndarray):
        input_features = np.array(input_features).reshape(1, -1)
    input_df = pd.DataFrame(input_features, columns=feature_names)
    scaled_features = scaler.transform(input_df)
    pred_label = model.predict(scaled_features)[0]
    pred_prob = model.predict_proba(scaled_features)[0][1]
    return pred_label, pred_prob

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Phishing Website Detector", page_icon="🛡️", layout="wide")
st.title("🛡️ Phishing Website Detection System")
st.markdown("""
Enter website feature values below to predict whether a website is **Legitimate** or **Phishing**.
""")

# Dynamic input form
user_inputs = []
st.subheader("Input Features")
cols = st.columns(3)  # 3 inputs per row for a cleaner layout
for idx, feature in enumerate(top_features_model_based):
    val = cols[idx % 3].number_input(f"{feature}", value=0.0, step=0.01, format="%.2f")
    user_inputs.append(val)

# Predict button
if st.button("Predict"):
    label, prob = predict_phishing_safe(user_inputs, best_model, scaler_model, top_features_model_based)
    st.success(f"Prediction: **{'Phishing' if label==1 else 'Legitimate'}**")
    st.info(f"Probability of being phishing: **{prob:.3f}**")

# Optional: Model info
with st.expander("ℹ️ Model Information"):
    st.markdown("""
    - Model: Random Forest Classifier (Top 15 Features)
    - Accuracy: 96.5%
    - F1 Score: 0.961
    - AUC: 0.994
    """)

# Footer
st.markdown("---")
st.markdown("Created by **Faheem Khan** | Apache 2.0 License")
