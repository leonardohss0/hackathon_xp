from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from werkzeug.security import generate_password_hash
from dash.exceptions import PreventUpdate

from app import *

# =========  Layout  =========== #
def render_layout(message):
    message = "Ocorreu algum erro durante o registro." if message == "error" else message

    layout = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                
                        html.Legend("Registre-se agora", style = {'margin':"0px 0px 30px 0px"}),
                        html.P("Nome"),
                        dbc.Input(id="user_register", placeholder="Digite seu nome completo", type="text", style = {'margin':"0px 0px 15px 0px"}),
                        html.P("E-mail"),
                        dbc.Input(id="email_register", placeholder="Digite seu e-mail", type="email", style = {'margin':"0px 0px 15px 0px", "width":"20vw"}),
                        html.P("Senha"),
                        dbc.Input(id="pwd_register", placeholder="Digite a sua senha", type="password"),
                        dbc.Button("Registrar", id='register-button', style={"margin": "20px 0px 10px 0px"}),
                        html.Span(message, style={"text-align": "center"}),

                        html.Div([
                            html.Label("Ou ", style={"margin-right": "5px"}),
                            dcc.Link("faça login", href="/login"),
                        ], style={"justify-content": "center", "display": "flex", "margin": "0px 0px 0px 0px"})
                ], className="align-self-center")

                ], md=4, className="align-self-center"),
                dbc.Col([], md=8, style = {'background-color':'#1010C5'})

            ], style={"height": "100vh"}),
        ], fluid=True)
    
    return layout


# =========  Callbacks Page1  =========== #
@app.callback(
    Output('register-state', 'data'),
    Input('register-button', 'n_clicks'), 

    [State('user_register', 'value'), 
    State('pwd_register', 'value'),
    State('email_register', 'value')],
    )
def successful(n_clicks, username, password, email):
    if n_clicks == None:
        raise PreventUpdate

    if username is not None and password is not None and email is not None:
        hashed_password = generate_password_hash(password, method='sha256')
        ins = Users_tbl.insert().values(username=username,  password=hashed_password, email=email)
        conn = engine.connect()
        conn.execute(ins)
        conn.close()
        return ''
    else:
        return 'error'