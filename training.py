from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib

def train_model(X_train, y_train, X_test, y_test):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    # Calculate training accuracy (on training set)
    y_train_pred = model.predict(X_train)
    accuracy_train = accuracy_score(y_train, y_train_pred)

    # Calculate test accuracy
    accuracy_test = accuracy_score(y_test, y_pred)

    # Save the trained model to a file
    joblib.dump(model, 'model.pkl')

    # Save accuracies to a file
    with open("accuracy.txt", "w") as f:
        f.write(f"Training Accuracy: {accuracy_train}\n")
        f.write(f"Test Accuracy: {accuracy_test}\n")

    print(f"Model trained successfully. Training Accuracy: {accuracy_train:.4f}, Test Accuracy: {accuracy_test:.4f}")
    return model, accuracy_train, accuracy_test


if __name__ == '__main__':
    # Example: Load sample data
    from sklearn.datasets import load_iris
    data = load_iris()
    X, y = data.data, data.target

    # Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    train_model(X_train, y_train, X_test, y_test)
