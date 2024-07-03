import os
import sys
import pandas as pd
from src.US_ElectricityPrice.exception import customexception
from src.US_ElectricityPrice.logger import logging
from src.US_ElectricityPrice.utils.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")
            
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            
            scaled_data=preprocessor.transform(features)
            
            pred=model.predict(scaled_data)
            
            return pred
            
            
        
        except Exception as e:
            raise customexception(e,sys)
    
    
    
class CustomData:
    def __init__(
                 self,
                 year:float,
                 month : float,
                 customers : float,
                 revenue : float,
                 sales : float,
                 stateDescription : str,
                 sectorName : str
                 :
        
        self.year=carat
        self.customers=customers
        self.revenue=revenue
        self.sales=sales
        self.stateDescription=stateDescription
        self.sectorName=sectorName
    )
                
    def get_data_as_dataframe(self):
            try:
                custom_data_input_dict = {
                    'year':[self.year],
                    'customers':[self.customers],
                    'revenue':[self.revenue],
                    'sales':[self.sales],
                    'stateDescription':[self.stateDescription],
                    'sectorName':[self.sectorName]
                }
                df = pd.DataFrame(custom_data_input_dict)
                logging.info('Dataframe Gathered')
                return df
            except Exception as e:
                logging.info('Exception Occured in prediction pipeline')
                raise customexception(e,sys)