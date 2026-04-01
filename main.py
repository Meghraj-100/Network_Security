from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig
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
        logging.info("Data Ingestion completed successfully.")
        data_validation_config=DataValidationConfig(training_pipeline_config=trainingpipeline_config)
        data_validation=DataValidation(data_ingestion_artifact=dataingestionartifact,data_validation_config=data_validation_config)
        logging.info("Data Validation component created successfully.")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation completed successfully.")
        print(dataingestionartifact)
        print(data_validation_artifact)


        # df=data_ingestion.export_collection_as_dataframe()
        # df=data_ingestion.export_data_to_feature_store(dataframe=df)
        # data_ingestion.split_data_as_train_test(dataframe=df)

    except Exception as e:
        logging.info("Error occurred: %s", e)
        raise NetworkSecurityException(e,sys)