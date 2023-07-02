from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash_bootstrap_templates import load_figure_template

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from dash.exceptions import PreventUpdate

# =========  Layout  =========== #
def render_layout():
    template = html.Div([
            dbc.Card([
                dcc.Location(id="data-url"), 
                html.Div([
                    html.Iframe(src='https://r2aubuvhy9q.typeform.com/c/DjIIB0vP', style= {'height':'80vh', 'width':'50vw', 'margin':'50px 0px 30px 0px'})
                ]),
                html.Div([
                    dbc.Button("Próximo", id="next-page"),            
                ])

            ], className="align-self-center")
        ])
    return template 

# =========  Callbacks Page1  =========== #
@app.callback(
    Output('data-url', 'pathname'),
    Input('next-page', 'n_clicks'), 
    )
def next_page(n_clicks):
    if n_clicks == None:
        raise PreventUpdate

    else:
        return '/home'