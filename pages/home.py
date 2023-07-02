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
                dcc.Location(id="home-url"), 
                html.P([
                    'Página home'
                ]),
                html.Div([
                    dbc.Button("Próximo", id="next-page"),            
                ])

            ], className="align-self-center")
        ])
    return template 

# =========  Callbacks Page1  =========== #
@app.callback(
    Output('home-url', 'pathname'),
    Input('logout_button', 'n_clicks'),
    )
def successful(n_clicks):
    if n_clicks == None:
        raise PreventUpdate
    
    return '/login'