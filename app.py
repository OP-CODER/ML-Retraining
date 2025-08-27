import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
from pipeline import pipeline

st.title("ML Model Retraining Pipeline")

jenkins_url = "http://localhost:8080/job/Retraining/build"  # Replace with your Jenkins URL
jenkins_user = "admin"  # Replace with Jenkins username
jenkins_token = "1168619df0b6d32a138ae59acde3ab5532"  # Replace with Jenkins API token

if st.button("Run Retraining Pipeline via Jenkins"):
    try:
        response = requests.post(jenkins_url, auth=HTTPBasicAuth(jenkins_user, jenkins_token))
        if response.status_code == 201:
            st.success("Jenkins job triggered successfully!")
        else:
            st.error(f"Failed to trigger Jenkins job: Status code {response.status_code}")
    except Exception as e:
        st.error(f"Error triggering Jenkins job: {e}")

st.write("---")

# Optional: Local pipeline run fallback
if st.button("Run Retraining Pipeline Locally"):
    accuracy = pipeline()
    st.write(f"Retraining completed locally! Model accuracy: {accuracy:.3f}")
