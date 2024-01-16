from src.code.constants import *
from src.code.utils.common import read_yaml, create_directories
from src.code.entity.entityconfig import (DataIngestionConfig,
                                            DataValidationConfig, DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
        keys_filepath = KEYS_FILE_PATH,
        param_filepath=PARAM_FILE_PATH
        ):

        self.config = read_yaml(config_filepath)
        self.schema=read_yaml(schema_filepath)
        self.param=read_yaml(param_filepath)
        self.keys = read_yaml(keys_filepath)

        create_directories([self.config.artifacts_root])

    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.dataset

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir ,
            s3_bucket=config.s3_bucket,
            s3_dataset=config.s3_dataset
        )
        return data_ingestion_config
    
    def get_keys(self):
        keys=self.keys
        return keys
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        schema =  self.schema.TARGET_COLUMN
        param=self.param.XGBoost

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            target_column = schema.name,
            n_estimators = param.n_estimators,
            max_depth = param.max_depth,
            learning_rate = param.learning_rate,
            subsample = param.subsample,
            colsample_bytree= param.colsample_bytree,
            reg_alpha= param.reg_alpha,
            reg_lambda= param.reg_lambda,
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        schema =  self.schema.TARGET_COLUMN
        param = self.param.XGBoost

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            parameters=param,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri="https://dagshub.com/sujith-kamme/Cross-Sell-Insight.mlflow"
        )

        return model_evaluation_config