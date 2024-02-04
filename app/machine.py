from pandas import DataFrame
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime
import joblib

""" Joblib is optimized to be fast, especially on large data sets,
    is robust to errors and can handle large datasets without crashing,
    can be used to save and load a variety of different object types,
    easy to use with a simple API
"""

class Machine:
    """ Instantiates and fits a RandomForestClassifier to make predictions"""
    def __init__(self, df: DataFrame):
        self.name = 'Random Forest Classifier'
        target = df['Rarity']
        features = df[['Level', 'Health', 'Energy', 'Sanity']]
        self.model = RandomForestClassifier()
        self.model.fit(features, target)
        self.time = datetime.now()

    def __call__(self, feature_basis: DataFrame):
        prediction = self.model.predict(feature_basis)[0]
        confidence = max(self.model.predict_proba(feature_basis)[0])
        return prediction, confidence

    """ Saves model to a file path to hold results """
    def save(self, filepath: str):
        filepath = r"C:\Users\akeps\PycharmProjects\BandersnatchStarter\app\model.joblib"
        joblib.dump(self, filepath)

    """ A STATIC Method belongs to a class, not a specific instance of that class. """
    @staticmethod
    def open(filepath: str):
        return joblib.load(filepath)

    def info(self):
        return f"Base Model: {self.name}<br>Timestamp: {self.time}"


