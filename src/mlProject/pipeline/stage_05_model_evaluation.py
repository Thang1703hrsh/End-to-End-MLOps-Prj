from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_evaluation import ModelEvaluation
from src.mlProject import logger
import os

STAGE_NAME = "Model evaluation stage"

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Thang1703hrsh/End-to-End-MLOps-Prj.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="Thang1703hrsh"
os.environ["MLFLOW_TRACKING_PASSWORD"]="ece30f068f3ab90db9c9eb11e94e0f5a953f95d2"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

