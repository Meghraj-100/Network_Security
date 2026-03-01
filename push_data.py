import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

import certifi
ca=certifi.where()

import pandas as pd
import pymongo
import numpy as np

from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract:
    def __init__(self):
        try:
            pass
            # self.client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            # logging.info("MongoDB client created successfully.")
        except Exception as e:
            #logging.error(f"Error creating MongoDB client: {e}")
            raise NetworkSecurityException(e, sys)

    
    
    def cv_to_json_convertor(self,file_path):
        try:
            df=pd.read_csv(file_path)
            df.reset_index(drop=True,inplace=True)

            records=list(json.loads(df.T.to_json()).values())
            logging.info(f"CSV file at {file_path} converted to JSON successfully.")
            return records
        
        except Exception as e:
            #logging.error(f"Error converting CSV to JSON: {e}")
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongo(self,records,database,collection):
        try:
            self.databse=database
            self.collection=collection
            self.records=records
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.databse=self.mongo_client[self.databse]
            self.collection=self.databse[self.collection]

            self.collection.insert_many(self.records)

            return (len(self.records))
        
           
        except Exception as e:
            #logging.error(f"Error inserting data into MongoDB: {e}")
            raise NetworkSecurityException(e, sys)


if __name__=="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="MEGHRAJNetworkSecurityDB"
    COLLECTION="NETWORKData"
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mongo(records=records,database=DATABASE,collection=COLLECTION)
    print(f"{no_of_records} records inserted successfully into MongoDB collection '{COLLECTION}' in database '{DATABASE}'.")