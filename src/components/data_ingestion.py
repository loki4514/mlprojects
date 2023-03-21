import os
import sys 
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# reading the data, saving the raw data, train and test data
@dataclass
# instead of defining a variable commong method
# is defining a fucntion (def) but using this contructor we directly define the variable
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifacts','train.csv')
    test_data_path : str=os.path.join('artifacts','test.csv')
    raw_data_path : str=os.path.join('artifacts','data.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion method or component")
        try:
            df = pd.read_csv('notebook\Stud.csv')
            logging.info("Read the data as a dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path,index = False,header=True)
            
            logging.info("Train test split initiated")
            
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header= True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e :
            raise CustomException(e,sys)
        
        
if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()