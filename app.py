import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('Sura.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Stock Market Next Day Close Prediction")

# Input fields
date_input = st.date_input("Date")
open_price = st.number_input("Open Price", min_value=0.0)
high_price = st.number_input("High Price", min_value=0.0)
low_price = st.number_input("Low Price", min_value=0.0)
close_price = st.number_input("Close Price", min_value=0.0)
volume = st.number_input("Volume", min_value=0)

# Convert date to UNIX timestamp
unix_date = int(np.datetime64(date_input).astype(np.int64) // 10**9)

# Predict button
if st.button("Predict Next Day Close"):
    input_data = [[unix_date, open_price, high_price, low_price, close_price, volume]]
    prediction = model.predict(input_data)
    st.success(f"Predicted Next Day Close Price: ${prediction[0]:.2f}")

