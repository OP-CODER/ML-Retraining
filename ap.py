def load_metrics():
    try:
        with open('/shared-volume/accuracy.txt', 'r') as f:
            return f.read()
    except Exception:
        return "Metrics not available"

st.write(load_metrics())
