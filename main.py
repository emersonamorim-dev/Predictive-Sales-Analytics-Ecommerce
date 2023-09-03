import os
import pandas as pd
import numpy as np

# Importações do Dash
import dash
import dash_core_components as dcc
import dash_html_components as html

# Inicialização do objeto app do Dash
app = dash.Dash(__name__)

# Definição da estrutura do layout do Dash (exemplo simples)
app.layout = html.Div([
    html.H1("Dashboard de Vendas - Ecommerce"),
    dcc.Graph(id='example-graph',
              figure={
                  'data': [
                      {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Predictive .Inc'},
                      {'x': [1, 2, 3], 'y': [7, 4, 5], 'type': 'bar', 'name': 'Emerson LTDA'},
                  ],
                  'layout': {
                      'title': 'Gráfico de Exemplo'
                  }
              })
])

def generate_sales_data():
    # Geração fictícia de dados
    num_entries = 1000
    df = pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', periods=num_entries, freq='D'),
        'sales': np.random.randint(50, 500, size=num_entries),
        'category': np.random.choice(['A', 'B', 'C'], num_entries)
    })

    # Salvar como sales_data.parquet
    if not os.path.exists('data'):
        os.makedirs('data')
    df.to_parquet('data/processed/sales_data.parquet')

def initialize_data():
    if not os.path.exists('data/processed/sales_data.parquet'):
        # Função para gerar dados fictícios e salvar como sales_data.parquet
        generate_sales_data()
    else:
        print("Dados já inicializados!")

def main():
    # Inicializar dados, se necessário
    initialize_data()

    # Iniciar o dashboard
    app.run_server(debug=True, port=8050)

if __name__ == "__main__":
    main()
