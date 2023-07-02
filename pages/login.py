from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *

import numpy as np
import plotly.express as px
from flask import session

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, LoginManager

from dash.exceptions import PreventUpdate

# =========  Layout  =========== #
def render_layout(message):
    message = "Ocorreu algum erro durante o login." if message == "error" else message
    login = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        html.Legend("Faça o login", style = {'margin':"0px 0px 30px 0px"}),
                        html.P("E-mail"),
                        dbc.Input(id="user_login", placeholder="Digite seu e-mail", type="text", style = {'margin':"0px 0px 15px 0px", "width":"20vw"}),
                        html.P("Senha"),
                        dbc.Input(id="pwd_login", placeholder="Digite sua senha", type="password"),
                        dbc.Button("Login", id="login_button", style={"margin": "20px 0px 10px 0px"}),
                        html.Span(message, style={"text-align": "center"}),
                        
                        html.Div([
                            html.Label("Ou", style={"margin-right": "5px"}),
                            dcc.Link("registre-se", href="/register"),
                        ], style={"justify-content": "center", "display": "flex", "margin": "0px 0px 0px 0px"})
                    ], class_name="align-self-center") 
                ], style={"height": "100vh"}, md=4, className="align-self-center"),
                dbc.Col([], md=8, style = {'background-color':'#1010C5'}),
        ])
    ], fluid=True)
    
    return login

# =========  Callbacks Page1  =========== #
@app.callback(
    Output('login-state', 'data'),

    Input('login_button', 'n_clicks'), 

    [State('user_login', 'value'), 
    State('pwd_login', 'value')],
    )
def successful(n_clicks, email, password):
    if n_clicks is None:
        raise PreventUpdate

    select_query = Users_tbl.select().where(Users_tbl.c.email == email)

    with engine.connect() as conn:
        result = conn.execute(select_query)
        row = result.fetchone()  # Retrieve the first row

        if row is not None:
            if check_password_hash(row.password, password):
                
                return "success"
            else:
                return "error"

        else:
            return "error"