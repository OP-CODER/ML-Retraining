from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Save the trained model to a file
    joblib.dump(model, 'model.pkl')
    
    return model

# Add code to load your training data and call train_model
if __name__ == '__main__':
    # Example: Load sample data (replace this with actual loading logic)
    from sklearn.datasets import load_iris
    data = load_iris()
    X_train, y_train = data.data, data.target
    
    train_model(X_train, y_train)
