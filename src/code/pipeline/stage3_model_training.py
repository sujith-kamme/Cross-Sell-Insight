from src.code.config.config import ConfigurationManager
from src.code.components.model_training import ModelTrainer
from src.code.logging import LogTool
from pathlib import Path


STAGE_NAME = "Model Training phase"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()

if __name__ == '__main__':
    try:
        LogTool.info(f"------------- {STAGE_NAME} started -------------")
        obj = ModelTrainerTrainingPipeline()
        obj.run()
        LogTool.info(f"------------- {STAGE_NAME} completed -----------")
    except Exception as e:
        LogTool.exception(e)
        raise e
