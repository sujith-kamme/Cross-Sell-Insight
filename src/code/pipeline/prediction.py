import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from pathlib import Path
import joblib

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_training/xg_boost.joblib'))

    def predict(self, data):
        pred = self.model.predict(data)
        pred_proba = self.model.predict_proba(data)
        print(pred_proba)
        if pred ==0:
            prob=pred_proba[0][0]
        else:
            prob=pred_proba[0][1]
        return pred,prob