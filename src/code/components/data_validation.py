import os
from src.code.logging import LogTool
from src.code.entity.entityconfig import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)[:-1]
            #print(all_cols)
            all_schema = self.config.all_schema.keys()
            #print(all_schema)
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                else:
                    validation_status = True
            return validation_status
        
        except Exception as e:
            raise e