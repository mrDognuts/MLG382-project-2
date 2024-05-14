
from dash.dependencies import Input, Output

error_type = {
    "NoneType": "All inputs must have a value",
    "NegNum": "All numeric inputs must be non-negative.",
    "NAE": ""
}

def validation_callback(app):

    @app.callback(
        Output("open-val-msg", "children"),
        Input("open-input", "value")
    )
    def validate_open(value):

        if value is None:
            return error_type["NoneType"]

        if value < 0:
            return error_type["NegNum"]

        return error_type["NAE"]


    @app.callback(
        Output("high-val-msg", "children"),
        Input("high-input", "value")
    )
    def validate_high(value):

        if value is None:
            return error_type["NoneType"]

        if value < 0:
            return error_type["NegNum"]

        return error_type["NAE"]


    @app.callback(
        Output("low-val-msg", "children"),
        Input("low-input", "value")
    )
    def validate_low(value):

        if value is None:
            return error_type["NoneType"]

        if value < 0:
            return error_type["NegNum"]

        return error_type["NAE"]

    @app.callback(
        Output("close-val-msg", "children"),
        Input("close-input", "value")
    )
    def validate_close(value):

        if value is None:
            return error_type["NoneType"]

        if value < 0:
            return error_type["NegNum"]

        return error_type["NAE"]
    

    @app.callback(
    Output("volume-val-msg", "children"),
    Input("volume-input", "value")
    )
    def validate_volume(value):

        if value is None:
            return error_type["NoneType"]

        if value < 0:
            return error_type["NegNum"]

        return error_type["NAE"]