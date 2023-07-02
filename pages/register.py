from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from werkzeug.security import generate_password_hash
from dash.exceptions import PreventUpdate

import warnings
warnings.filterwarnings("ignore")

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
                        dbc.Input(id="user_register", placeholder="Digite seu nome completo", type="text", style = {'margin':"0px 0px 15px 0px", 'background-color':"#FFFBFB"}),
                        html.P("E-mail"),
                        dbc.Input(id="email_register", placeholder="Digite seu e-mail", type="email", style = {'margin':"0px 0px 15px 0px", "width":"20vw", 'background-color':"#FFFBFB"}),
                        html.P("Senha"),
                        dbc.Input(id="pwd_register", placeholder="Digite a sua senha", type="password", style={'background-color':"#FFFBFB"}),
                        dbc.Button("Registrar", id='register-button', style={"margin": "20px 0px 10px 0px"}),
                        html.Span(message, style={"text-align": "center"}),

                        html.Div([
                            html.Label("Ou ", style={"margin-right": "5px"}),
                            dcc.Link("faça login", href="/login"),
                        ], style={"justify-content": "center", "display": "flex", "margin": "0px 0px 0px 0px"})
                ], className="align-self-center",  style = {'background-color':"#FFF6F6"})

                ], md=4, className="align-self-center",  style = {'background-color':"#FFF6F6"}),
                dbc.Col([
                    html.Div([
                        html.Video(
                            src="/assets/xp-educacao-manifesto-16x9-720p-3_XDV6sgha.mp4",
                            autoPlay=True,
                            loop=True,
                            muted=True,
                            style={
                                "width": "100%",
                                "height": "100%",
                                "object-fit": "cover",
                                "filter": "brightness(70%)", 
                            }
                        )
                    ], style={"height": "100vh"})  
            ], style={"height": "100vh", 'background-color':"#000000"}, md=8)
        ],  style = {'background-color':"#FFF6F6"})
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