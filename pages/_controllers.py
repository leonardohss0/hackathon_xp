from dash import html, dcc
import dash_bootstrap_components as dbc

controllers = dbc.Row([
                dcc.Store(id='store-global'),
                # html.Img(id="logo", src=app.get_asset_url("logo_dark.png"), style={'width':'50%'}),
                html.H3("Vendas de imóveis - NYC", style={"margin-top": "30px"}),
                html.P(
                """Utilize este dashboard para analisar vendas ocorridas na 
                cidade de New York no período de 1 ano. """
                )
    ])

    

