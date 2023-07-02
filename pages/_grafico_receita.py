import pandas as pd
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc


# Sample data
data = pd.date_range(start='2022-01-01', end='2022-12-31', freq='M')
revenue = [100, 150, 200, 180, 220, 250, 230, 280, 300, 270, 250, 200]
expenses = [80, 120, 150, 130, 160, 180, 170, 190, 210, 200, 180, 150]

# Create dataframe
df = pd.DataFrame({'Date': data, 'Revenue': revenue, 'Expenses': expenses})

# Create bar chart
fig = go.Figure()

# Add revenue bars
fig.add_trace(go.Bar(
    x=df['Date'],
    y=df['Revenue'],
    name='Receitas',
    marker_color='green',
    opacity=0.5
))

# Add expenses bars
fig.add_trace(go.Bar(
    x=df['Date'],
    y=df['Expenses'],
    name='Despesas',
    marker_color='red',
    opacity=0.5
))

# Customize layout
fig.update_layout(
    barmode='group',
    title='Receitas x Despesas no período',
    showlegend=True,
    plot_bgcolor='white'
)

hist = dbc.Row([
                dcc.Graph(id="hist-graph", figure=fig)
                ], style={"height": "40vh"})