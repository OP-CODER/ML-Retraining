import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
from pipeline import pipeline

st.title("ML Model Retraining Pipeline")

jenkins_url_base = "http://localhost:8080"  # Jenkins base URL
job_name = "Retraining"
jenkins_user = "admin"
jenkins_token = "1193221706f44c4de96c269d2982546ade"

def get_crumb():
    crumb_url = f"{jenkins_url_base}/crumbIssuer/api/json"
    try:
        resp = requests.get(crumb_url, auth=HTTPBasicAuth(jenkins_user, jenkins_token))
        if resp.status_code == 200:
            data = resp.json()
            return {data['crumbRequestField']: data['crumb']}
        else:
            st.error(f"Failed to get crumb: {resp.status_code}")
            return {}
    except Exception as e:
        st.error(f"Error getting crumb: {e}")
        return {}

if st.button("Run Retraining Pipeline via Jenkins"):
    build_url = f"{jenkins_url_base}/job/{job_name}/build"
    crumb_header = get_crumb()
    try:
        response = requests.post(build_url,
                                 auth=HTTPBasicAuth(jenkins_user, jenkins_token),
                                 headers=crumb_header)
        if response.status_code in [201, 200]:
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

