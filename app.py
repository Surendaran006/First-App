import streamlit as st
import numpy as np
import pickle
from datetime import date

# Load the trained model
with open('Sura.pkl', 'rb') as file:
    model = pickle.load(file)

# --- Page Config ---
st.set_page_config(page_title="📈 Master Stock Predictor", layout="wide")

# --- Theme Toggle ---
theme_mode = st.radio("🌗 Select Theme", ["Light", "Dark"], horizontal=True)

# --- Font Style Toggle ---
font_style = st.selectbox("🔢 Number Font Style", ["Digital", "Monospace", "Bold"])

# --- Background Theme (Weather Mode) ---
weather = st.selectbox("🌦️ Choose Weather Mode", ["Clear", "Rainy", "Snowy", "Sunset"])

# --- Custom Styling Based on Selections ---
bg_image = {
    "Clear": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
    "Rainy": "https://i.gifer.com/7VE.gif",
    "Snowy": "https://i.gifer.com/ZZ5H.gif",
    "Sunset": "https://images.unsplash.com/photo-1501973801540-537f08ccae7f"
}[weather]

# Color Themes
text_color = "#ffffff" if theme_mode == "Dark" else "#000000"
bg_color = "#0e0e0e" if theme_mode == "Dark" else "#f5f5f5"

# Font Styles
font_family = {
    "Digital": "'Courier New', monospace",
    "Monospace": "monospace",
    "Bold": "'Segoe UI', sans-serif"
}[font_style]

# --- Apply All CSS ---
st.markdown(f"""
    <style>
    body {{
        background-image: url('{bg_image}');
        background-size: cover;
        background-attachment: fixed;
        color: {text_color};
    }}
    .title {{
        font-size: 40px;
        font-weight: bold;
        color: {text_color};
        text-align: center;
        margin-bottom: 5px;
    }}
    .subtitle {{
        text-align: center;
        color: {text_color};
        font-size: 16px;
        margin-bottom: 40px;
    }}
    .digital-output {{
        font-family: {font_family};
        font-size: 42px;
        color: #00ffcc;
        background-color: black;
        padding: 15px 30px;
        border-radius: 10px;
        display: inline-block;
        margin-top: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- UI Title ---
st.markdown('<div class="title">📊 Stock Market Predictor - Master Edition</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Weather Effects | Light/Dark Mode | Styled Prediction | Notes</div>', unsafe_allow_html=True)

# --- Input Form ---
with st.form("predict_form"):
    col1, col2 = st.columns(2)
    with col1:
        date_input = st.date_input("📅 Date", value=date.today())
        open_price = st.number_input("Open Price", min_value=0.0, format="%.2f")
        high_price = st.number_input("High Price", min_value=0.0, format="%.2f")
    with col2:
        low_price = st.number_input("Low Price", min_value=0.0, format="%.2f")
        close_price = st.number_input("Close Price", min_value=0.0, format="%.2f")
        volume = st.number_input("Volume", min_value=0)

    # Notes area
    st.markdown("🗒️ **Write your market notes:**")
    notes = st.text_area("Notes", placeholder="Eg: Market may rise due to Fed meeting...")

    # Buttons
    col3, col4 = st.columns([1, 1])
    with col3:
        predict_btn = st.form_submit_button("🚀 Predict")
    with col4:
        reset_btn = st.form_submit_button("🔄 Reset")

# --- Reset Action ---
if reset_btn:
    st.experimental_rerun()

# --- Prediction Logic ---
if predict_btn:
    unix_date = int(np.datetime64(date_input).astype(np.int64) // 10**9)
    input_data = [[unix_date, open_price, high_price, low_price, close_price, volume]]
    prediction = model.predict(input_data)

    st.markdown("### ✅ **Predicted Close Price for Next Day**")
    st.markdown(f'<div class="digital-output">${prediction[0]:.2f}</div>', unsafe_allow_html=True)
