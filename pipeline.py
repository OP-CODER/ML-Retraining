from data_loader import load_data
from preprocessing import preprocess_data
from training import train_model
from evaluation import evaluate_model
from model_storage import save_model

def pipeline(data_path='training_data.csv'):
    data = load_data(data_path)
    X_train, X_test, y_train, y_test, scaler = preprocess_data(data, 'target')
    model = train_model(X_train, y_train)
    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Evaluation accuracy: {accuracy}")
    if accuracy > 0.8:
        save_model(model, scaler)
    else:
        print("Model performance below threshold, skipping save.")
    return accuracy

if __name__ == "__main__":
    pipeline()
