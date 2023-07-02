from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import *
import dash_dangerously_set_inner_html
import dash_table

from pages._sidebar import sidebar
from pages._chatgpt import chatgpt
from pages._grafico_receita import hist
from pages._figura_rosca import rosc

import warnings
warnings.filterwarnings("ignore")

from dash.exceptions import PreventUpdate

# Define the expense data
expense_data = [
    {'Categoria': 'Habitação ou aluguel', 'Valor gasto': 'R$ 500,00'},
    {'Categoria': 'Energia', 'Valor gasto': 'R$ 50,00'},
    {'Categoria': 'Gás', 'Valor gasto': 'R$ 50,00'},
    {'Categoria': 'Internet', 'Valor gasto': 'R$ 50,00'},
    {'Categoria': 'Educação', 'Valor gasto': 'R$ 500,00'},
    {'Categoria': 'Alimentação', 'Valor gasto': 'R$ 500,00'},
    {'Categoria': 'Lazer e cultura', 'Valor gasto': 'R$ 500,00'},
    {'Categoria': 'Transporte', 'Valor gasto': 'R$ 500,00'}
]


# =========  Layout  =========== #
def render_layout(df_typeform, str_openai):

    template = dbc.Container(
        children=[
            dcc.Location(id="home-url"),

            dbc.Row([
                dbc.Col([
                        sidebar
                ], md = 12, style = {'height':'90px'}),
                
                dbc.Col([
                    chatgpt,
                    html.P(dash_dangerously_set_inner_html.DangerouslySetInnerHTML(str_openai.replace('\n', "<br>")), style={"padding":"15px"})
                ], md=4, style = {"height":"90vh"}),
                
                dbc.Col([
                    dbc.Row([
                        dbc.Col(
                            hist, md = 12),
                        dbc.Col(rosc, md = 6),
                        dbc.Col(html.Div([
                            html.H6('Detalhes das Despesas'),
                            dash_table.DataTable(
                                id='expense-table',
                                columns=[{'name': col, 'id': col} for col in expense_data[0].keys()],
                                data=expense_data,
                                style_header={'backgroundColor': 'rgb(230, 230, 230)'},
                                style_cell={'textAlign': 'left'},
                                style_data_conditional=[
                                    {'if': {'row_index': 'odd'}, 'backgroundColor': '#FFFFFF'}
                                ]
                            )
                        ], style={'padding':'30px'}), md = 6),
                        html.P("Adicione as suas despesas e suas receitas na plataforma para acompanhar sua evolução mensal")
                    ])
                ], md=8)

        ])

        ], fluid=True)
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