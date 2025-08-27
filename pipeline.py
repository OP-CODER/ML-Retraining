from data_loader import load_data
from preprocessing import preprocess_data
from training import train_model
from evaluation import evaluate_model
from model_storage import save_model

def pipeline(data_path='training_data.csv'):
    # Load and preprocess data
    data = load_data(data_path)
    X_train, X_test, y_train, y_test, scaler = preprocess_data(data, 'target')
    
    # Train model and get training accuracy
    model, accuracy_train, accuracy_test = train_model(X_train, y_train, X_test, y_test)
    
    # Evaluate model (can use same accuracy_test)
    accuracy_eval = evaluate_model(model, X_test, y_test)
    
    print(f"Training accuracy: {accuracy_train:.4f}")
    print(f"Evaluation accuracy: {accuracy_eval:.4f}")
    
    # Save model if evaluation performance is good
    if accuracy_eval > 0.8:
        save_model(model, scaler)
    else:
        print("Model performance below threshold, skipping save.")
    
    return accuracy_eval

if __name__ == "__main__":
    pipeline()
