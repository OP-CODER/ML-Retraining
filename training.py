from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib

def train_model(X_train, y_train, X_test, y_test):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Save the trained model to a file
    joblib.dump(model, 'model.pkl')

    # Save accuracy to a file
    with open("accuracy.txt", "w") as f:
        f.write(str(accuracy))

    print(f"Model trained successfully. Accuracy: {accuracy:.4f}")
    return model, accuracy


if __name__ == '__main__':
    # Example: Load sample data (replace with your actual loading logic)
    from sklearn.datasets import load_iris
    data = load_iris()
    X, y = data.data, data.target

    # Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    train_model(X_train, y_train, X_test, y_test)
