# Stroke Prediction System

![Screenshot 1](test-cases/Screenshot%20from%202024-07-29%2016-37-11.png)
![Screenshot 2](test-cases/Screenshot%20from%202024-07-29%2016-38-00.png)

## Overview
The Stroke Prediction System is a machine learning project designed to predict the likelihood of a stroke occurring based on various health and demographic factors. This project aims to provide a reliable tool for early detection and prevention of strokes, thereby aiding healthcare professionals in making informed decisions.

## Features
- Predicts the risk of stroke based on user inputs.
- Uses a machine learning model trained on a large dataset of health records.
- Easy-to-use interface for healthcare professionals and patients.
- Provides visualizations to understand the impact of different factors on stroke risk.

## Dataset
The dataset used for training the model contains 40,910 entries and 11 columns. The features include:
- `sex`
- `age`
- `hypertension`
- `heart_disease`
- `ever_married`
- `work_type`
- `Residence_type`
- `avg_glucose_level`
- `bmi`
- `smoking_status`

The target variable is `stroke`.

## Installation
To run the Stroke Prediction System locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/siddhantbhattarai/stroke-prediction-system.git
    ```
2. Navigate to the project directory:
    ```bash
    cd stroke-prediction-system
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```bash
    python app.py
    ```

## Usage
- Open a web browser and go to `http://127.0.0.1:5000/`.
- Enter the required information in the input fields.
- Click on the "Predict" button to get the stroke risk prediction.
- View the results and visualizations.

## Model
The prediction model is built using a Support Vector Machine (SVM) algorithm. The model file `svm_model.pkl` is stored in the `models` directory.

## Screenshots
![Screenshot 1](test-cases/Screenshot%20from%202024-07-29%2016-37-11.png)
![Screenshot 2](test-cases/Screenshot%20from%202024-07-29%2016-38-00.png)

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

