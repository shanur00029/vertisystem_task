
import os
import sys
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.US_ElectricityPrice.exception import customexception
from src.US_ElectricityPrice.logger import logging

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder 

from src.US_ElectricityPrice.utils.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("read train and test data complete")
                        
            logging.info("Applying preprocessing object on training and testing datasets.")
            label_encoder = LabelEncoder()
            train_df['sectorName'] = label_encoder.fit_transform(train_df['sectorName'])
            train_df['stateDescription']= label_encoder.fit_transform(train_df['stateDescription'])
            train_df.drop(['customers','revenue','sales'],axis=1,inplace= True)
            train_arr = train_df

            test_df['sectorName'] = label_encoder.fit_transform(train_df['sectorName'])
            test_df['stateDescription']= label_encoder.fit_transform(train_df['stateDescription'])
            test_df.drop(['customers','revenue','sales'],axis=1,inplace= True)
            
            test_arr = test_df

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            logging.info("preprocessing pickle file saved")
            
            return (
                train_arr,
                test_arr
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)
if __name__ == '__main__':
    obj = DataTransformation()
    obj.initialize_data_transformation(r'C:\Users\shanu\Desktop\vertisystem\U.S.ElectricityPrices\artifacts\train.csv',r'C:\Users\shanu\Desktop\vertisystem\U.S.ElectricityPrices\artifacts\test.csv')