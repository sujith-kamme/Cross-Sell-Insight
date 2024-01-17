from flask import Flask, render_template, request, jsonify
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.code.pipeline.prediction import PredictionPipeline

app = Flask(__name__,static_url_path="/static")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        gender = int(request.form['gender'])
        age = float(request.form['age'])
        driving_license = int(request.form['driving_license'])
        region_code = float(request.form['region_code'])
        previously_insured = int(request.form['previously_insured'])
        vehicle_age = float(request.form['vehicle_age'])
        vehicle_damage = int(request.form['vehicle_damage'])
        annual_premium = float(request.form['annual_premium'])
        policy_sales_channel = float(request.form['policy_sales_channel'])
        vintage = float(request.form['vintage'])

        data = np.array([gender, age, driving_license, region_code, previously_insured, vehicle_age,
                         vehicle_damage, annual_premium, policy_sales_channel, vintage]).reshape(1, -1)

        obj = PredictionPipeline()
        prediction, probability = obj.predict(data)
        if prediction==0:
            prediction_text = f"Based on model prediction, There is a chance of {round(probability*100,2)}% that the customer might not find the Cross-Sell pitch appealing."
        else:
            prediction_text = f"Based on model prediction, There is a chance of {round(probability*100,2)}% that the customer might be interested in the Cross-Sell pitch."
        return jsonify({'prediction_text': prediction_text})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run()
