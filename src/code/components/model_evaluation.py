import os
import pandas as pd
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from src.code.entity.entityconfig import ModelEvaluationConfig
from src.code.utils.common import save_json
from pathlib import Path
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from dataclasses import asdict

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self,actual, pred):
        acc = accuracy_score(actual,pred)*100
        precision = precision_score(actual,pred)
        recall = recall_score(actual,pred)
        f1=f1_score(actual,pred)
        roc_auc = roc_auc_score(actual, pred)
        return acc,precision,recall,f1,roc_auc
    


    def setup_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]


        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            y_pred = model.predict(test_x)

            acc,precision,recall,f1_score,roc_auc = self.eval_metrics(test_y, y_pred)
            
            scores = {"Accuracy": acc, "Precision": precision, "Recall": recall,"F1 Score": f1_score,"ROC AUC Score": roc_auc}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            xgb_params=model.get_params()
            mlflow.log_params({f"{param}": value for param, value in xgb_params.items()})

            mlflow.log_metric("Accuracy", acc)
            mlflow.log_metric("Precision", precision)
            mlflow.log_metric("Recall", recall)
            mlflow.log_metric("F1 score", f1_score)
            mlflow.log_metric("ROC AUC score",roc_auc)


            if tracking_url_type_store != "file":

                #Model Registry
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="XGBoost")
            else:
                mlflow.sklearn.log_model(model, "model")