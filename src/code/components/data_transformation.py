import os
from src.code.logging import LogTool
from sklearn.model_selection import train_test_split
import pandas as pd
from src.code.entity.entityconfig import DataTransformationConfig
from sklearn.preprocessing import LabelEncoder

class DataTransformationTraining:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        
        data=self.transform(data)
        
        train, test = train_test_split(data,random_state=12)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        LogTool.info("Splited data into training and test sets")
        LogTool.info(train.shape)
        LogTool.info(test.shape)
    
    def transform(self,df):
        le = LabelEncoder()
        df['Gender']=le.fit_transform(df['Gender'])
        df['Vehicle_Damage']=le.fit_transform(df['Vehicle_Damage'])
        df["Vehicle_Age"] = df["Vehicle_Age"].replace({"< 1 Year":0,"1-2 Year":1, "> 2 Years":2})
        return df
    
class DataTransformationProd:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def transform(self):
        data = pd.read_csv(self.config.data_path)
        data=self.transform(data)
        data.to_csv(os.path.join(self.config.root_dir, "transformed_data.csv"),index = False)
