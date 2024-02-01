import sys, os
sys.path.append(os.path.dirname('src\mlProject'))
from mlProject import logger

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = DataIngestionTrainingPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nXXXXXXXX")
except Exception as e:
   logger.exception(e)
   raise e