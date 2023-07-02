import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc

# Expenses data
categories = ['Habitação ou aluguel', 'Energia', 'Gás', 'Internet', 'Educação',
              'Alimentação', 'Lazer e cultura', 'Transporte', 'Dívidas ou financiamentos', 'Outras despesas']
expenses = [500, 50, 50, 50, 500, 500, 500, 500, 0, 0]

# Sort expenses and categories in descending order
sorted_expenses, sorted_categories = zip(*sorted(zip(expenses, categories), reverse=True))

# Create bar chart
fig = go.Figure(data=[go.Bar(
    y=sorted_categories,
    x=sorted_expenses,
    orientation='h',
    marker_color='red',  # Set the color of the bars to red
    opacity=0.5  # Set the opacity of the bars to 0.5
)])

# Customize layout
fig.update_layout(
    title='Despesas por categoria',
    plot_bgcolor='white',
    bargap=0.2,  # Set the gap between bars
    yaxis=dict(autorange='reversed')  # Reverse the y-axis to display categories from top to bottom
)

rosc = dbc.Row([
                dcc.Graph(id="rosc-graph", figure=fig)
                ], style={"height": "40vh"})