import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

def fit_linear_regression(data, prediction_cols, target_col):

    X = data[prediction_cols]
    y = data[target_col ]
    
    # create model
    model = LinearRegression()
    model.fit(X, y)  # Fit model

    return model


def make_linear_regression_prediction(model, row, prediction_basis_cols):    
    # Make prediction
    prediction = model.predict(row[prediction_basis_cols].values.reshape(1, -1))
    
    return prediction[0]