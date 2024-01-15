from src.code.config.config import ConfigurationManager
from src.code.components.data_ingestion import DataIngestion
from src.code.components.data_validation import DataValidation
from src.code.logging import LogTool

STAGE_NAME = "Data Ingestion and Validation stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    def run(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        aws_keys=config.get_keys()
        data_ingestion = DataIngestion(config=data_ingestion_config,keys=aws_keys)
        data_ingestion.download_file_from_s3()
        data_ingestion.extract_zip_file()

class DataValidationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        check=data_validation.validate_all_columns()
        return check


if __name__ == '__main__':
    try:
        LogTool.info(f"--------------- {STAGE_NAME} started ---------------")
        di_obj = DataIngestionPipeline()
        di_obj.run()
        dv_obj=DataValidationPipeline()
        check=dv_obj.run()
        if check:
            LogTool.info(f"--------------- {STAGE_NAME} finished ---------------")
        else:
            LogTool.info(f"--------------- Columns Mismatch. Please check the data file ---------------")
    except Exception as e:
        LogTool.exception(e)
        raise e