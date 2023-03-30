import os,sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from sklearn.metrics import r2_score,mean_absolute_error

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_model


@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join('artifacts','model.pkl')
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        
    def initiate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info("splitting training and test input data")
            x_train,y_train,x_test,y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )
            # after converting the data into machine level 
            models = {
                "Linear Regression":LinearRegression(),
                "K-Neighbours ":KNeighborsRegressor(),
                "Random Forest": RandomForestRegressor(),
                "Decision Tree" : DecisionTreeRegressor(),
                "Gradient Boosting" : GradientBoostingRegressor(),
                "Catboost ": CatBoostRegressor(verbose=False),
                "Xgboost":XGBRegressor(),
                "Adaboost":AdaBoostRegressor()
                
            }
        # 
            model_report:dict = evaluate_model(x_train=x_train,y_train=y_train,x_test=x_test,y_test=y_test,models = models)
            
            best_model_score = max(sorted(model_report.values()))
            
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]
            
            if best_model_score < 0.60:
                raise CustomException("No best Model found")
            logging.info(f"best model found")
            
            
            save_object (
                file_path= self.model_trainer_config.trained_model_path,
                obj = best_model
            )
            
            predicted = best_model.predict(x_test)
            r2_scoring = r2_score(y_test,predicted)
            
            return r2_scoring
            
        except Exception as e:
            raise CustomException(e,sys)