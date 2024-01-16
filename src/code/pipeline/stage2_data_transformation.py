from src.code.config.config import ConfigurationManager
from src.code.components.data_transformation import DataTransformationTraining
from src.code.logging import LogTool
from pathlib import Path




STAGE_NAME = "Data Transformation phase"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def run(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformationTraining(config=data_transformation_config)
            data_transformation.train_test_spliting()

        except Exception as e:
            print(e)



if __name__ == '__main__':
    try:
        LogTool.info(f"---------------- {STAGE_NAME} started ----------------")
        obj = DataTransformationTrainingPipeline()
        obj.run()
        LogTool.info(f"---------------- {STAGE_NAME} finished ----------------")
    except Exception as e:
        LogTool.exception(e)
        raise e