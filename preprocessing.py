from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, target_column):
    # Drop rows with missing target
    df = df.dropna(subset=[target_column])

    # Fill missing values in features with median
    df = df.fillna(df.median())

    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler
