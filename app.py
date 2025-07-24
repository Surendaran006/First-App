import streamlit as st
import numpy as np
import pickle
from datetime import date

# Load the trained model
with open('Sura.pkl', 'rb') as file:
    model = pickle.load(file)

# Page config
st.set_page_config(page_title="🌟 Sura Stock Master", layout="wide")

# --- User Choices ---
theme = st.radio("🌗 Theme", ["Light", "Dark"], horizontal=True)
weather = st.selectbox("⛅ Weather", ["Clear", "Rainy", "Snowy", "Sunset"])
font_style = st.selectbox("🔤 Font Style", ["Digital", "Monospace", "Bold"])

# Background images for weather
weather_backgrounds = {
    "Clear": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
    "Rainy": "https://i.gifer.com/7VE.gif",
    "Snowy": "https://i.gifer.com/ZZ5H.gif",
    "Sunset": "https://images.unsplash.com/photo-1501973801540-537f08ccae7f"
}
bg_url = weather_backgrounds[weather]

# Font CSS
font_family = {
    "Digital": "'Courier New', monospace",
    "Monospace": "monospace",
    "Bold": "'Segoe UI', sans-serif"
}[font_style]

# Theme Colors
text_color = "#fff" if theme == "Dark" else "#000"
panel_color = "#000000cc" if theme == "Dark" else "#ffffffcc"

# --- Custom CSS ---
st.markdown(f"""
    <style>
    .main-container {{
        background: url("{bg_url}") no-repeat center center fixed;
        background-size: cover;
        padding: 20px;
        border-radius: 12px;
        color: {text_color};
    }}
    .title {{
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        color: {text_color};
    }}
    .digital {{
        font-family: {font_family};
        font-size: 38px;
        color: #00ffee;
        background: black;
        padding: 15px 30px;
        display: inline-block;
        border-radius: 10px;
        margin-top: 20px;
    }}
    .glass-panel {{
        background: {panel_color};
        padding: 20px;
        border-radius: 15px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- UI START ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="title">📈 Sura’s Stock Market Master Predictor</div>', unsafe_allow_html=True)

st.markdown('<div class="glass-panel">', unsafe_allow_html=True)

# --- Form Inputs ---
with st.form("form"):
    col1, col2 = st.columns(2)
    with col1:
        date_input = st.date_input("📅 Date", value=date.today())
        open_price = st.number_input("Open Price", min_value=0.0, format="%.2f")
        high_price = st.number_input("High Price", min_value=0.0, format="%.2f")
    with col2:
        low_price = st.number_input("Low Price", min_value=0.0, format="%.2f")
        close_price = st.number_input("Close Price", min_value=0.0, format="%.2f")
        volume = st.number_input("Volume", min_value=0)

    # Notes
    notes = st.text_area("🗒️ Notes", placeholder="Enter your market thoughts here...")

    # Buttons
    col3, col4 = st.columns(2)
    with col3:
        predict = st.form_submit_button("🚀 Predict")
    with col4:
        reset = st.form_submit_button("🔄 Reset")

st.markdown('</div>', unsafe_allow_html=True)  # Close glass panel

# Reset
if reset:
    st.experimental_rerun()

# Prediction logic
if predict:
    unix_date = int(np.datetime64(date_input).astype(np.int64) // 10**9)
    input_data = [[unix_date, open_price, high_price, low_price, close_price, volume]]
    prediction = model.predict(input_data)
    st.markdown("### ✅ **Predicted Next Day Close Price:**")
    st.markdown(f'<div class="digital">${prediction[0]:.2f}</div>', unsafe_allow_html=True)

# End main container
st.markdown('</div>', unsafe_allow_html=True)
