import streamlit as st
from pipeline import pipeline

st.title("ML Model Retraining Pipeline")

if st.button("Run Retraining Pipeline"):
    accuracy = pipeline()
    st.write(f"Retraining completed! Model accuracy: {accuracy:.3f}")
