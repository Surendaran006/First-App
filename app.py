import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('Sura.pkl', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("📈 Stock Market - Next Day Close Price Prediction")

# Sidebar for user inputs
st.sidebar.header("Enter Stock Data")

# Input fields
date_input = st.sidebar.date_input("📅 Date")
open_price = st.sidebar.number_input("Open Price", min_value=0.0, format="%.2f")
high_price = st.sidebar.number_input("High Price", min_value=0.0, format="%.2f")
low_price = st.sidebar.number_input("Low Price", min_value=0.0, format="%.2f")
close_price = st.sidebar.number_input("Close Price", min_value=0.0, format="%.2f")
volume = st.sidebar.number_input("Volume", min_value=0)

# Convert date to UNIX timestamp
unix_date = int(np.datetime64(date_input).astype(np.int64) // 10**9)

# Predict button
if st.sidebar.button("🚀 Predict Next Day Close"):
    input_data = [[unix_date, open_price, high_price, low_price, close_price, volume]]
    prediction = model.predict(input_data)
    st.success(f"📊 Predicted Next Day Close Price: **${prediction[0]:.2f}**")
