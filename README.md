# Cross-Sell-Insight

Creating a predictive machine learning model to determine customer receptiveness to cross-sell pitches.

## **Coding Workflow:**

### Project Setup
1. Virtual environment (venv) created.
2. Automated project file structure creation - `template.py`.
3. Updated `requirements.txt` and `setup.py`.
4. Installed packages in venv
    ```bash
    pip install -r requirements.txt
    ``` 

### **Pipelines Implementation**
1. Implemented custom logging functionality for the project under `src/code/logging/__init__.py`.
2. Implemented common utility functions under `utils/common.py`.

**Data Ingestion and Validation**
1. Updated `config.yaml`.
2. Updated `schema.yaml`.
3. Updated `constants/__init__.py`.
4. Updated `entity/entityconfig.py`.
5. Updated `src/code/config/config.py`.
6. Updated `components/data_ingestion.py`.
7. Updated `components/data_validation.py`.
8. Updated `pipeline/stage1_data_ingestion_and_validation.py`.
9. Updated `main.py` file.

**Data Transformation**
1. Updated `config.yaml`.
2. Updated `schema.yaml`.
3. Updated `entity/entityconfig.py`.
4. Updated `src/code/config/config.py`.
5. Updated `components/data_transformation.py`.
7. Updated `pipeline/stage2_data_transformation.py`.
8. Updated `main.py` file.

**Model Training**
1. Updated `config.yaml`.
2. Updated `entity/entityconfig.py`.
3. Updated `src/code/config/config.py`.
4. Updated `components/model_training.py`.
5. Updated `pipeline/stage3_model_training.py`.
6. Updated `main.py` file.
7. Updated `param.yaml`

**Setup remote access to enable collaboration** - with DagsHub

    Used MLFlow for 
    1. Experiment Tracking
    2. Upload model to model registry
    3. Model serving

**Model Evaluation**
1. Updated `config.yaml`.
2. Updated `entity/entityconfig.py`.
3. Updated `src/code/config/config.py`.
4. Updated `components/model_evaluation.py`.
5. Updated `pipeline/stage4_model_evaluation.py`.
6. Setting up MLFlow Tracking URI to enable collaboration
    Run this to export as env variables:

    ```bash

    export MLFLOW_TRACKING_URI= "https://dagshub.com/sujith-kamme/Cross-Sell-Insight.mlflow"

    export MLFLOW_TRACKING_USERNAME= "sujith-kamme"
    ```
7. Updated `main.py` file.



