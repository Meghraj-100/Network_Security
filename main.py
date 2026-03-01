from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys


if __name__=="__main__":
    try:
        trainingpipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config=trainingpipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("Data Ingestion component created successfully.")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)


        # df=data_ingestion.export_collection_as_dataframe()
        # df=data_ingestion.export_data_to_feature_store(dataframe=df)
        # data_ingestion.split_data_as_train_test(dataframe=df)

    except Exception as e:
        logging.info("Error occurred: %s", e)
        raise NetworkSecurityException(e,sys)