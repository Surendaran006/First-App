import streamlit as st
import numpy as np
import pickle

# Load model
with open('Sura.pkl', 'rb') as file:
    model = pickle.load(file)

# Page config
st.set_page_config(page_title="Stock Predictor Classic UI", layout="centered")

# Custom Classic Styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            font-size: 40px;
            font-weight: bold;
            color: #333333;
            text-align: center;
            margin-top: 20px;
        }
        .sub-text {
            text-align: center;
            color: #666;
            font-size: 16px;
            margin-bottom: 40px;
        }
        .stButton>button {
            background-color: #2b7de9;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">📊 Stock Market Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Predict the next day close price using market data</div>', unsafe_allow_html=True)

# Inputs
st.header("📥 Enter Today's Market Data")
col1, col2 = st.columns(2)

with col1:
    date_input = st.date_input("Date")
    open_price = st.number_input("Open Price", min_value=0.0, format="%.2f")
    high_price = st.number_input("High Price", min_value=0.0, format="%.2f")
    
with col2:
    low_price = st.number_input("Low Price", min_value=0.0, format="%.2f")
    close_price = st.number_input("Close Price", min_value=0.0, format="%.2f")
    volume = st.number_input("Volume", min_value=0)

# Convert date to UNIX
unix_date = int(np.datetime64(date_input).astype(np.int64) // 10**9)

# Predict button
st.markdown("### 📈 Prediction Result")
if st.button("Predict Next Day Close"):
    input_data = [[unix_date, open_price, high_price, low_price, close_price, volume]]
    prediction = model.predict(input_data)
    st.success(f"✅ Predicted Next Day Close Price: **${prediction[0]:.2f}**")
