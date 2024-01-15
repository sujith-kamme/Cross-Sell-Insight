from src.code.constants import *
from src.code.utils.common import read_yaml, create_directories
from src.code.entity.entityconfig import (DataIngestionConfig,
                                            DataValidationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAM_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH,
        keys_filepath = KEYS_FILE_PATH
        ):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)
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
    