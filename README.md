# 🛡️ Phishing Website Detector

## 🌐 Live Demo

You can try the phishing detection web app online here:  
[Phishing Website Detector - Live](https://phisingwebsitedetectionsytem.streamlit.app/)


A simple and interactive **web app** to detect whether a website is **Phishing** or **Legitimate** using a machine learning model trained on top features. Built with **Streamlit** for a clean and user-friendly interface.

---

## 🚀 Features

- **Real-time manual input:** Enter feature values for a website and get instant prediction.  
- **Confidence level:** Shows the probability of the website being phishing.  
- **Attractive UI:** Color-coded cards for phishing (red) and legitimate (green) websites.  
- **Optimized model:** Uses top 15 features selected via Random Forest feature importance for fast and accurate predictions.  
- **Easy to deploy:** Lightweight app, ready for production or personal use.

---

## 💻 How to Use

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**:

```bash
streamlit run app.py
```

4. **Open in browser**  
After running, Streamlit will provide a local URL (usually `http://localhost:8501`) where you can access the app.

---

## 🧩 Input Features

The app uses the following **top 15 features** for prediction:

- SSLfinal_State  
- URL_of_Anchor  
- web_traffic  
- Prefix_Suffix  
- having_Sub_Domain  
- age_of_domain  
- Page_Rank  
- Links_in_tags  
- Domain_registeration_length  
- Request_URL  
- Links_pointing_to_page  
- DNSRecord  
- Google_Index  
- URL_Length  
- HTTPS_token  

> **Note:** You don’t need to worry about all 30 original features; the top 15 features give almost the same performance with faster predictions.

---

## 📊 Model Performance

| Metric     | Score |
|------------|-------|
| Accuracy   | 96.5% |
| Precision  | 95.9% |
| Recall     | 96.3% |
| F1-Score   | 96.1% |
| AUC-ROC    | 0.994 |

> The top-feature model achieves nearly the same performance as the full model while being faster and easier to maintain.

---

## ⚙️ Technology Stack

- **Python 3.x**  
- **Scikit-learn** → Machine learning & preprocessing  
- **Streamlit** → Web app interface  
- **Joblib** → Saving/loading trained models  
- **Numpy & Pandas** → Data handling

---

## 📝 How It Works

1. User enters feature values for a website in the UI.  
2. Values are scaled using the trained `StandardScaler`.  
3. Scaled features are fed into the trained **Random Forest model**.  
4. Model outputs prediction (`Phishing` or `Legitimate`) and confidence score.  
5. Result is displayed in a clean, color-coded card.

---

## 📦 Files in the Repository

- `app.py` → Streamlit application code  
- `best_phishing_model.pkl` → Trained Random Forest model  
- `best_scaler.pkl` → Scaler used to normalize inputs  
- `requirements.txt` → Python dependencies

---

## 🎯 Future Improvements

- Allow **URL input** and automatically extract features.  
- Add **dark mode toggle** for better user experience.  
- Deploy on **Heroku** or **Streamlit Cloud** for public access.

---

## ⚡ Author

**Faheem Khan** – Machine Learning Enthusiast & Developer

---

## 📝 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

