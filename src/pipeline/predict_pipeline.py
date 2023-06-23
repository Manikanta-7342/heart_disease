import sys
import os
import pandas as pd
from src.exceptions import CustomException
from src.util import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            features = pd.read_csv('sample.csv')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            print(data_scaled)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        age: int,
        sex: str,
        chest_pain: str,
        resting_bp: int,
        cholesterol: float,
        fasting_bs: str,
        max_hr: float,
        resting_ecg: str,
        st_slope:str,
        oldpeak: float,
        exercise_angina: str):

        self.age = age

        self.sex = sex

        self.chest_pain = chest_pain

        self.fasting_bs = fasting_bs

        self.resting_bp = resting_bp

        self.cholesterol = cholesterol

        self.max_hr = max_hr

        self.resting_ecg = resting_ecg

        self.st_slope = st_slope

        self.oldpeak = oldpeak

        self.exercise_angina = exercise_angina

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Age": [self.age],
                "Sex": [self.sex],
                "ChestPainType": [self.chest_pain],
                "RestingBP": [self.resting_bp],
                "Cholesterol": [self.cholesterol],
                "FastingBS": [self.fasting_bs],
                "RestingECG": [self.resting_ecg],
                "MaxHR": [self.max_hr],
                "ExerciseAngina": [self.exercise_angina],
                "Oldpeak": [self.oldpeak],
                "ST_Slope": [self.st_slope]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
