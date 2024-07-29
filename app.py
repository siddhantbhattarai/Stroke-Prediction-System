from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('models/rf_model.pkl', 'rb'))

# Load the StandardScaler
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    age = float(request.form['age'])
    sex = float(request.form['sex'])
    hypertension = int(request.form['hypertension'])
    heart_disease = int(request.form['heart_disease'])
    ever_married = int(request.form['ever_married'])
    work_type = int(request.form['work_type'])
    residence_type = int(request.form['Residence_type'])
    avg_glucose_level = float(request.form['avg_glucose_level'])
    bmi = float(request.form['bmi'])
    smoking_status = int(request.form['smoking_status'])

    # Create input array for prediction
    input_features = np.array([[age, sex, hypertension, heart_disease, ever_married, work_type,
                                residence_type, avg_glucose_level, bmi, smoking_status]])

    # Scale the input features
    input_features_scaled = scaler.transform(input_features)

    # Make prediction
    prediction = model.predict(input_features_scaled)
    probability = model.predict_proba(input_features_scaled)[0][1] * 100
    output = 'likely' if prediction[0] == 1 else 'unlikely'

    return jsonify(prediction=output, probability=round(probability, 2))

if __name__ == "__main__":
    app.run(debug=True)
