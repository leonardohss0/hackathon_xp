from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import *
import time

import warnings
warnings.filterwarnings("ignore")

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
                    dbc.Button("Começar a Organizar", id="next-page", style={'margin':'0px 0px 0px 50px'}),            
                ], id= 'div-botao', style={'display': 'none'})

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
    

@app.callback(Output('div-botao', 'style'),
              Input('div-botao', 'n_clicks'))
def show_button(n_clicks):
    if n_clicks is None:
        time.sleep(30)
        return {'display': 'block'}
    else:
        return {'display': 'none'}