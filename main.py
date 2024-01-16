from src.code.logging import LogTool
from src.code.pipeline.stage1_data_ingestion_and_validation import DataIngestionPipeline, DataValidationPipeline
from src.code.pipeline.stage2_data_transformation import DataTransformationTrainingPipeline

stage_1="Data Ingestion and Validation"

try:
    LogTool.info(f"----------- {stage_1} phase started -----------")
    data_ingestion=DataIngestionPipeline()
    data_ingestion.run()
    
    data_validation=DataValidationPipeline()
    check=data_validation.run()
    if check:
        LogTool.info(f"--------------- {stage_1} finished ---------------")
    else:
        LogTool.info(f"--------------- Columns Mismatch. Please check the data file ---------------")

except Exception as e:
    LogTool.exception(e)
    raise e

stage_2 = "Data Transformation"
try:
   LogTool.info(f"----------- {stage_1} phase started -----------") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.run()
   LogTool.info(f"--------------- {stage_1} finished ---------------")
except Exception as e:
        LogTool.exception(e)
        raise e