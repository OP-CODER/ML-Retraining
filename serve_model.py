from flask import Flask, request, jsonify
import joblib  # or pickle, depending on your model saving method

app = Flask(__name__)

# Load your trained model (replace 'model.pkl' with your actual model filename)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = data['features']  # expecting a list of feature values

    # Make prediction
    prediction = model.predict([features])

    # Return prediction result as JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
