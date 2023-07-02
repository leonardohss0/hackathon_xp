from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *

import warnings
warnings.filterwarnings("ignore")

from werkzeug.security import check_password_hash

from dash.exceptions import PreventUpdate

# =========  Layout  =========== #
def render_layout(message):
    message = "Ocorreu algum erro durante o login." if message == "error" else message
    login = dbc.Container(
        children=[
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        
                        html.H3([
                                'Bem-vindo à Organiz',
                                html.Span(
                                    'AI',
                                    style={
                                        "font-weight": "bold",
                                        "background-color": "#FFB8B8",
                                        "border": "2px solid #FF9F9F",
                                        "border-radius":"4px",
                                        "padding": "4px",
                                    }
                                )
                            ]),

                        html.P("Powered by ChatGPT and Pig", style = {'margin':"0px 0px 75px 0px", "font-style":"italic"}),
                        html.Legend("Faça o login", style = {'margin':"0px 0px 30px 0px"}),
                        html.P("E-mail"),
                        dbc.Input(id="user_login", placeholder="Digite seu e-mail", type="text", style = {'margin':"0px 0px 15px 0px", "width":"20vw", 'background-color':"#FFFBFB"}),
                        html.P("Senha"),
                        dbc.Input(id="pwd_login", placeholder="Digite sua senha", type="password", style={'background-color':"#FFFBFB"}),
                        dbc.Button("Login", id="login_button", style={"margin": "20px 0px 10px 0px"}),
                        html.Span(message, style={"text-align": "center"}),
                        
                        html.Div([
                            html.Label("Ou", style={"margin-right": "5px"}),
                            dcc.Link("registre-se", href="/register"),
                        ], style={"justify-content": "center", "display": "flex", "margin": "0px 0px 0px 0px"})
                    ], class_name="align-self-center", style = {'background-color':"#FFF6F6"})
                ], style={"height": "100vh", 'background-color':"#FFF6F6"}, md=4, className="align-self-center"),
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
        ])
    ], fluid=True)
    
    return login

# =========  Callbacks Page1  =========== #
@app.callback(
    [Output('login-state', 'data'), Output('login-value', 'data')],

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
                
                return "success", email
            else:
                return "error", email

        else:
            return "error", email