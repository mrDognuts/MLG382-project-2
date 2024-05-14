# Import necessary libraries
import pandas as pd

import dash
from dash import dcc, html

# custom callbacks for dash
from callbacks import (
    validation as val,
    predict as pred
)

# Supress warnings
import warnings
warnings.simplefilter(action="ignore", category=Warning)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define color scheme
colors = {
    "background": "#f9f9f9",  # Light gray background
    "text": "#333333",        # Dark gray text color
    "accent": "#4CAF50",      # Green accent color
    "button": "#FF5733",      # Orange button color
}

# html.Div(style={"marginBottom": "20px"}, children=[

app.layout = html.Div(style={"backgroundColor": colors["background"], "padding": "20px"}, children=[

    html.H1("Market Cap Prediction", style={"color": colors["text"], "textAlign": "center"}),

    # style={"color": "red", "marginTop": "10px"}

    html.Div(id="open-val-msg", style={"color": "red", "marginTop": "10px"}),
    html.Div(style={"marginBottom": "20px"}, children=[
        html.Label("Open: ", style={"color": colors["text"]}),
        dcc.Input(id="open-input", type="number", value=0),
    ]),

    html.Div(id="high-val-msg", style={"color": "red", "marginTop": "10px"}),
    html.Div(style={"marginBottom": "20px"}, children=[
        html.Label("High: ", style={"color": colors["text"]}),
        dcc.Input(id="high-input", type="number", value=0),
    ]),

    html.Div(id="low-val-msg", style={"color": "red", "marginTop": "10px"}),
    html.Div(style={"marginBottom": "20px"}, children=[
        html.Label("Low: ", style={"color": colors["text"]}),
        dcc.Input(id="low-input", type="number", value=0),
    ]),

    html.Div(id="close-val-msg", style={"color": "red", "marginTop": "10px"}),
    html.Div(style={"marginBottom": "20px"}, children=[
        html.Label("Close: ", style={"color": colors["text"]}),
        dcc.Input(id="close-input", type="number", value=0),
    ]),

    html.Div(id="volume-val-msg", style={"color": "red", "marginTop": "10px"}),
    html.Div([
        html.Label("Volume: ", style={"color": colors["text"]}),
        dcc.Input(id="volume-input", type="number", value=0),
    ]),
    
    html.Button("Predict", id="predict-button", n_clicks=0, style={"backgroundColor": colors["button"], "color": "#FFFFFF", "marginTop": "20px"}),
    html.Div(id="output-prediction", style={"marginTop": "20px", "fontWeight": "bold", "fontSize": "18px", "color": colors["accent"], "textAlign": "center"})
])

val.validation_callback(app)
pred.predict_callback(app)

if __name__ == "__main__":
    app.run_server(debug=True)