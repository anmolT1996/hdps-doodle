from django.apps import AppConfig
from django.conf import settings
import os
import joblib
import numpy as np

class HdpsConfig(AppConfig):
    name = 'hdps'
    path = os.path.join(settings.ML_MODEL_DIR, 'test.pkl')
    path2 = os.path.join(settings.ML_MODEL_DIR, 'trained_data.pkl')
    classifier = joblib.load(path)
    trained_data = joblib.load(path2)
