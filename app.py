import streamlit as st
import numpy as np
import pickle

# Load model
with open('Sura.pkl', 'rb') as file:
    model = pickle.load(file)

# Page config
st.set_page_config(page_title="Stock Predictor 🌧️", layout="wide")
st.title("📈 Stock Market - Next Day Close Price Prediction")

# Weather selector
theme = st.selectbox("Choose Theme 🌤️", ["Default", "Rainy", "Winter", "Summer"])

# --- RAIN DROPS EFFECT ---
if theme == "Rainy":
    st.markdown(
        """
        <style>
        body {
            background: #0e0e0e;
            overflow: hidden;
        }
        .rain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9999;
        }
        .drop {
            position: absolute;
            bottom: 100%;
            width: 2px;
            height: 15px;
            background: rgba(255, 255, 255, 0.4);
            animation: fall 1s linear infinite;
        }
        @keyframes fall {
            to {
                transform: translateY(100vh);
            }
        }
        </style>
        <div class="rain">
        """ + 
        ''.join([f'<div class="drop" style="left:{i}%; animation-delay: {i*0.03}s;"></div>' for i in range(100)]) +
        """
        </div>
        """, 
        unsafe_allow_html=True
    )

# --- Inputs in Sidebar ---
st.sidebar.header("Enter Stock Data")

date_input = st.sidebar.date_input("📅 Date")
open_price = st.sidebar.number_input("Open Price", min_value=0.0)
high_price = st.sidebar.number_input("High Price", min_value=0.0)
low_price = st.sidebar.number_input("Low Price", min_value=0.0)
close_price = st.sidebar.number_input("Close Price", min_value=0.0)
volume = st.sidebar.number_input("Volume", min_value=0)

# Convert date
unix_date = int(np.datetime64(date_input).astype(np.int64) // 10**9)

# Predict button
if st.sidebar.button("🚀 Predict Next Day Close"):
    input_data = [[unix_date, open_price, high_price, low_price, close_price, volume]]
    prediction = model.predict(input_data)
    st.success(f"📊 Predicted Next Day Close Price: **${prediction[0]:.2f}**")
