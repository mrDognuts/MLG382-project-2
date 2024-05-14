import pandas as pd

from dash.dependencies import Input, Output, State

import joblib
from pathlib import Path

# Load Model
path_to_model = str(Path(__file__).parents[2])
path_to_model += "/artifacts/model.sav"

model = joblib.load(path_to_model)

def predict_callback(app):

    # Define callback function to handle user input and generate prediction
    @app.callback(
        Output("output-prediction", "children"),

        [Input("predict-button", "n_clicks")],
        [State("open-input", "value"),
        State("high-input", "value"),
        State("low-input", "value"),
        State("close-input", "value"),
        State("volume-input", "value"),]
    )
    def predict_market_cap(n_clicks, open, high, low, close, volume):
        
        input_data = pd.DataFrame({
            "Open": [open],
            "High":[high],
            "Low": [low],
            "Close": [close],
            "Volume": [volume]
        })
        
        # Make predictions
        prediction = model.predict(input_data)[0]*-1
        return f"Prediction: {prediction}"