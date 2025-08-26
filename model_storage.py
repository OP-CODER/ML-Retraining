import joblib
import os
from datetime import datetime

def save_model(model, scaler, model_dir='models'):
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_path = os.path.join(model_dir, f"model_{timestamp}.joblib")
    scaler_path = os.path.join(model_dir, f"scaler_{timestamp}.joblib")
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
    print(f"Saved model to {model_path}")
    print(f"Saved scaler to {scaler_path}")
