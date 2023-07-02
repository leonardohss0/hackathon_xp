from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

chatgpt = dbc.Row([
        dcc.Store(id='store-global'),
        html.H3("Olá Leonardo!", style={"margin": "30px 0px 0px 20px"}),
        html.P(
        """De acordo com as informações que coletamos do seu perfil, separamos algumas recomendações que vão te auxiliar a economizar mais dinheiro e a investir melhor. """
        , style={"padding":"30px 30px 0px 30px"}),
         
    ])