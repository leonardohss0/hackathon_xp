from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash
import pandas as pd
import json

from app import *
from utils.openai import openai_responses, openai_responses_metas_individuais
from utils.typeform import typeform_responses, typeform_fields
from pages import login, data, register, home

import warnings
warnings.filterwarnings("ignore")

login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'

# =========  Layout  =========== #
app.layout = html.Div(
    children=[
                
        dbc.Col([
            dcc.Location(id="base-url", refresh=False), 
            dcc.Store(id="login-state", data=""),
            dcc.Store(id="register-state", data=""),
            dcc.Store(id="login-value", data = ""),

            html.Div(id="page-content", style={"height": "100vh", "display": "flex", "justify-content": "center"})
        ])
                    
    ])

# =========  Callbacks Page1  =========== #
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.callback(Output("base-url", "pathname"), 
            [
                Input("login-state", "data"),
                Input("register-state", "data")
            ])
def render_page_content(login_state, register_state):
    ctx = dash.callback_context
    if ctx.triggered:
        trigg_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if trigg_id == 'login-state' and login_state == "success":
            return '/data'
        if trigg_id == 'login-state' and login_state == "success":
            return '/home'
        if trigg_id == 'login-state' and login_state == "error":
            return '/login'
        

        elif trigg_id == 'register-state':
            print(register_state, register_state=='')
            if register_state == "":
                return '/login'
            else:
                return '/register'
    else:
        return '/'


@app.callback(Output("page-content", "children"), 
            Input("base-url", "pathname"),
            [State("login-state", "data"), State("register-state", "data"), State("login-value", "data"),])

def render_page_content(pathname, login_state, register_state, login_value):

    if (pathname == "/login" or pathname == "/"):
        return login.render_layout(login_state)

    if pathname == "/register":
        return register.render_layout(register_state)

    if pathname == "/data":
        return data.render_layout()
    
    if pathname == "/home":

        res_typeform_responses = typeform_responses()
        res_typeform_fields = typeform_fields()
     
        df_typeform = pd.merge(res_typeform_fields, res_typeform_responses, on = 'ref')

        data_dict = df_typeform.to_dict(orient='records')
        data_str = json.dumps(data_dict, ensure_ascii=False)
        response_openai =  openai_responses(data_str)
        response_metas_individuais = '' # openai_responses_metas_individuais(data_str)

        return home.render_layout(df_typeform, response_openai)

if __name__ == "__main__":
    app.run_server(port=8050, debug=True)