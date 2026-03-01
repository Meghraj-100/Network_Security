import os
import sys
import pandas as pd

import numpy as np


TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str= "Artifact"
FILE_NAME: str = "phisingData.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


DATA_INGESTION_COLLECTION_NAME = "NETWORKData"
DATA_INGESTION_DATABASE_NAME = "MEGHRAJNetworkSecurityDB"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION :float=0.2