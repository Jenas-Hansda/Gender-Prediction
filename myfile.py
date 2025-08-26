# app.py

import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("gender_predict.pkl", "rb") as f:
    model = pickle.load(f)

# Title of the app
st.title("Gender Predictor Based on Height and Weight")

# User input
height = st.number_input("Enter Height (in cm):", min_value=100, max_value=250, value=170)
weight = st.number_input("Enter Weight (in kg):", min_value=30, max_value=200, value=70)

# Prediction button
if st.button("Predict Gender"):
    input_data = np.array([[height, weight]])
    result = model.predict(input_data)

    if result[0][0]:  # Female is the first column in one-hot encoding
        st.success("Predicted Gender: Female")
    else:
        st.success("Predicted Gender: Male")
