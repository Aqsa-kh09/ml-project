import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("rf_best_model.pkl")

# App title
st.title("CTG Fetal State Prediction App")

st.write("Enter patient CTG values below")

# Input fields
LB = st.number_input("Baseline FHR")
AC = st.number_input("Accelerations")
FM = st.number_input("Fetal Movements")
UC = st.number_input("Uterine Contractions")
ASTV = st.number_input("ASTV")
MSTV = st.number_input("MSTV")
ALTV = st.number_input("ALTV")
MLTV = st.number_input("MLTV")

# Feature array
features = np.array([[LB, AC, FM, UC, ASTV, MSTV, ALTV, MLTV]])

# Predict button
if st.button("Predict"):

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Fetal State: Normal")

    elif prediction[0] == 2:
        st.warning("Fetal State: Suspect")

    else:
        st.error("Fetal State: Pathologic")