from src.code.config.config import ConfigurationManager
from src.code.components.model_evaluation import ModelEvaluation
from src.code.logging import LogTool

STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.setup_mlflow()



if __name__ == '__main__':
    try:
        LogTool.info(f"------------- {STAGE_NAME} started -------------")
        obj = ModelEvaluationPipeline()
        obj.run()
        LogTool.info(f"------------- {STAGE_NAME} completed -----------")
    except Exception as e:
        LogTool.exception(e)
        raise e