import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from sklearn.externals import joblib

# Inicialize o app Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Carregue os dados
data = pd.read_parquet("/data/processed/sales_data.parquet")
X = data.drop("sales", axis=1)

# Carregue o modelo
model = joblib.load("/models/sales_regression_model.pkl")
predictions = model.predict(X)

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Análise de Vendas E-commerce"), width={'size': 6, 'offset': 3}),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='sales-graph'), width=12),
    ]),
    dbc.Row([
        dbc.Col(html.P("Use o slider abaixo para ajustar o período de tempo:"), width={'size': 4, 'offset': 4}),
    ]),
    dbc.Row([
        dbc.Col(dcc.RangeSlider(
            id='date-slider',
            min=0,
            max=len(data) - 1,
            value=[0, len(data) - 1],
            marks={i: date for i, date in enumerate(data['date'].dt.strftime('%Y-%m-%d'))},
            step=None
        ), width=12),
    ]),
])

@app.callback(
    Output('sales-graph', 'figure'),
    [Input('date-slider', 'value')]
)
def update_graph(date_range):
    filtered_data = data.iloc[date_range[0]: date_range[1], :]
    trace1 = go.Scatter(x=filtered_data['date'], y=filtered_data['sales'], mode='lines', name='Vendas Reais')
    trace2 = go.Scatter(x=filtered_data['date'], y=predictions[date_range[0]: date_range[1]], mode='lines', name='Previsões')

    layout = go.Layout(title="Vendas vs Previsões", xaxis={'title': "Data"}, yaxis={'title': "Vendas"})
    return {'data': [trace1, trace2], 'layout': layout}

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)
