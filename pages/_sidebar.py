from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

sidebar = dbc.Row([
            dcc.Store(id='store-global'),
            dbc.Col(html.Legend([
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
                ], style = {'margin':"20px"}), md = 2),
            dbc.Col([
                dbc.Col([
                        dbc.Button([
                        "Página inicial"
                        ], className = "btn-header", style = {'margin':"20px"}),
                        dbc.Button([
                        "Extrato"
                        ], className = "btn-header", style = {'margin':"20px"}),
                        dbc.Button([
                        "Carteira Pig"
                        ], className = "btn-header", style = {'margin':"20px"}),
                        dbc.Button([      
                        "Gestão de ativos"
                        ], className = "btn-header", style = {'margin':"20px"}),
                        dbc.Button([   
                        "Configurações"
                        ], className = "btn-header", style = {'margin':"20px"})
                ], md=10, style = {"display": "flex", "justify-content": "right"}),
            ], md = 10)
        ])