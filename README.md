# Cross-Sell-Insight

Creating a predictive machine learning model to determine customer receptiveness to cross-sell pitches.
![UI](https://github.com/sujith-kamme/Cross-Sell-Insight/assets/142932988/e062a15e-8bcc-48d4-bb18-b7563a3a781f)

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

**Setup remote access to enable collaboration** - with DagsHub(MLflow)

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


## **AWS-CICD-Deployment-with-Github-Actions**

### 1. Login to AWS console.

### 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
### 3. Create ECR repo to store/save docker image
    - Save the URI

	
### 4. Create EC2 machine (Ubuntu) 

### 5. Open EC2 and Install docker in EC2 Machine:

	#optional
	sudo apt-get update -y
	sudo apt-get upgrade
	
	#required
	curl -fsSL https://get.docker.com -o get-docker.sh
	sudo sh get-docker.sh
	sudo usermod -aG docker ubuntu
	newgrp docker
	
### 6. Configure EC2 as self-hosted runner:

    Go to Settings>Actions>Runners>New self-hosted runner> choose os> then run the commands one after the other


### 7. Setup github secrets:

    Go to settings> Secrets and Variables > New repository secret 
    
    AWS_ACCESS_KEY_ID

    AWS_SECRET_ACCESS_KEY

    AWS_REGION = us-east-2

    AWS_ECR_LOGIN_URI = (sample)566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app


<img width="468" alt="CICD" src="https://github.com/sujith-kamme/Cross-Sell-Insight/assets/142932988/73182206-d4e3-4588-8f9e-269bb0b71164">


