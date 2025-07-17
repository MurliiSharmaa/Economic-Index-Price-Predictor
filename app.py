# app.py
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('index_price_model.pkl')

st.title("Economic Index Price Prediction")

st.write("Provide the following economic indicators:")

# User inputs
interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=20.0, value=3.0, step=0.1)
unemployment_rate = st.number_input("Unemployment Rate (%)", min_value=0.0, max_value=50.0, value=5.0, step=0.1)

if st.button("Predict Index Price"):
    input_data = np.array([[interest_rate, unemployment_rate]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Index Price: {prediction:.2f}")
