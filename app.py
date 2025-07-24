import streamlit as st
import numpy as np
import pickle

# Load model
with open('Sura.pkl', 'rb') as file:
    model = pickle.load(file)

# App Title
st.set_page_config(page_title="Stock Predictor 🌦️", layout="wide")
st.title("📈 Stock Market - Next Day Close Price Prediction")

# --- Weather Theme Selection ---
theme = st.selectbox("Choose Theme 🌤️", ["Default", "Rainy", "Winter", "Summer"])

# --- Apply Weather Themes using HTML/CSS ---
if theme == "Rainy":
    st.markdown("""
        <style>
        body {
            background-image: url("https://i.gifer.com/7VE.gif");
            background-size: cover;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

elif theme == "Winter":
    st.markdown("""
        <style>
        body {
            background-image: url("https://i.gifer.com/ZZ5H.gif");
            background-size: cover;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

elif theme == "Summer":
    st.markdown("""
        <style>
        body {
            background: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
        }
        </style>
        """, unsafe_allow_html=True)

# Sidebar Inputs
st.sidebar.header("Enter Stock Data")

date_input = st.sidebar.date_input("📅 Date")
open_price = st.sidebar.number_input("Open Price", min_value=0.0)
high_price = st.sidebar.number_input("High Price", min_value=0.0)
low_price = st.sidebar.number_input("Low Price", min_value=0.0)
close_price = st.sidebar.number_input("Close Price", min_value=0.0)
volume = st.sidebar.number_input("Volume", min_value=0)

# Date to Unix
unix_date = int(np.datetime64(date_input).astype(np.int64) // 10**9)

# Predict Button
if st.sidebar.button("🚀 Predict Next Day Close"):
    input_data = [[unix_date, open_price, high_price, low_price, close_price, volume]]
    prediction = model.predict(input_data)
    st.success(f"📊 Predicted Next Day Close Price: **${prediction[0]:.2f}**")
