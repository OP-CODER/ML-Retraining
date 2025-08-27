import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

st.title("ML Model Retraining Pipeline")

jenkins_url_base = "http://192.168.137.1:8080"
job_name = "Retraining"
jenkins_user = "admin"
jenkins_token = "1193221706f44c4de96c269d2982546ade"

def get_crumb():
    crumb_url = f"{jenkins_url_base}/crumbIssuer/api/json"
    try:
        response = requests.get(crumb_url, auth=HTTPBasicAuth(jenkins_user, jenkins_token))
        response.raise_for_status()
        data = response.json()
        return {data['crumbRequestField']: data['crumb']}
    except Exception as ex:
        st.error(f"Failed to get Jenkins crumb: {ex}")
        return {}

if st.button("Run Retraining Pipeline via Jenkins"):
    build_url = f"{jenkins_url_base}/job/{job_name}/build"
    crumb_header = get_crumb()
    try:
        response = requests.post(build_url,
                                 auth=HTTPBasicAuth(jenkins_user, jenkins_token),
                                 headers=crumb_header)
        if response.status_code in [200, 201]:
            st.success("Jenkins job triggered successfully!")
        else:
            st.error(f"Failed to trigger Jenkins job: {response.status_code} - {response.text}")
    except Exception as ex:
        st.error(f"Error triggering Jenkins job: {ex}")

st.write("---")

# Optional local fallback
from pipeline import pipeline
if st.button("Run Retraining Pipeline Locally"):
    accuracy = pipeline()
    st.write(f"Retraining completed locally! Model accuracy: {accuracy:.3f}")

