import joblib
import pandas as pd
import numpy as np

def predict_mental_health(input_data):
    # Load artifacts
    models = joblib.load('mental_health_models.pkl')
    scaler = joblib.load('scaler.pkl')
    
    # Preprocess input
    input_df = pd.DataFrame([input_data])
    processed = pd.get_dummies(input_df)
    
    # Align columns with training data
    train_cols = joblib.load('train_columns.pkl')
    processed = processed.reindex(columns=train_cols, fill_value=0)
    
    # Scale features
    scaled_input = scaler.transform(processed)
    
    # Predict
    predictions = {}
    for target, model in models.items():
        proba = model.predict_proba(scaled_input)[0][1]
        predictions[target] = {'prediction': model.predict(scaled_input)[0],
                              'probability': round(proba, 2)}
    
    return predictions