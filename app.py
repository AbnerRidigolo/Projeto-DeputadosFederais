import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date
import os
import sys

# Adicionar o diretório raiz ao path para importar módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.analysis.eda import load_processed_data, generate_eda_plots

# Carregar os dados processados
df = load_processed_data("../../data/processed")

# Inicializar a aplicação Dash
app = dash.Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    html.H1("Dashboard de Despesas dos Deputados Federais", 
            style={'textAlign': 'center', 'marginBottom': 30}),
    
    html.Div([
        html.Div([
            html.Label("Filtrar por Data:"),
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date=df['DataDocumento'].min(),
                end_date=df['DataDocumento'].max(),
                display_format='DD/MM/YYYY'
            )
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            html.Label("Filtrar por Tipo de Despesa:"),
            dcc.Dropdown(
                id='tipo-despesa-dropdown',
                options=[{'label': 'Todos', 'value': 'Todos'}] + 
                        [{'label': tipo, 'value': tipo} for tipo in df['TipoDespesa'].unique()],
                value='Todos',
                multi=True
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ], style={'marginBottom': 30}),
    
    html.Div([
        html.Div([
            dcc.Graph(id='despesas-por-tipo')
        ], style={'width': '50%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='despesas-por-deputado')
        ], style={'width': '50%', 'display': 'inline-block'})
    ]),
    
    html.Div([
        html.Div([
            dcc.Graph(id='despesas-ao-longo-tempo')
        ], style={'width': '50%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='despesas-por-uf')
        ], style={'width': '50%', 'display': 'inline-block'})
    ]),
    
    html.Div([
        dcc.Graph(id='distribuicao-valores')
    ], style={'width': '100%', 'marginTop': 20})
])

# Callback para atualizar os gráficos com base nos filtros
@app.callback(
    [Output('despesas-por-tipo', 'figure'),
     Output('despesas-por-deputado', 'figure'),
     Output('despesas-ao-longo-tempo', 'figure'),
     Output('despesas-por-uf', 'figure'),
     Output('distribuicao-valores', 'figure')],
    [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input('tipo-despesa-dropdown', 'value')]
)
def update_graphs(start_date, end_date, selected_tipos):
    # Filtrar dados por data
    filtered_df = df[(df['DataDocumento'] >= start_date) & (df['DataDocumento'] <= end_date)]
    
    # Filtrar por tipo de despesa
    if 'Todos' not in selected_tipos:
        filtered_df = filtered_df[filtered_df['TipoDespesa'].isin(selected_tipos)]
    
    # Gráfico 1: Despesas por tipo
    df_tipo = filtered_df.groupby('TipoDespesa')['ValorDocumento'].sum().reset_index()
    fig1 = px.bar(df_tipo, x='TipoDespesa', y='ValorDocumento',
                  title='Despesas Totais por Tipo de Despesa',
                  labels={'TipoDespesa': 'Tipo de Despesa', 'ValorDocumento': 'Valor Total (R$)'},
                  color='TipoDespesa')
    fig1.update_layout(xaxis_tickangle=45)
    
    # Gráfico 2: Top 10 deputados
    df_deputado = filtered_df.groupby('NomeDeputado')['ValorDocumento'].sum().nlargest(10).reset_index()
    fig2 = px.bar(df_deputado, x='NomeDeputado', y='ValorDocumento',
                  title='Top 10 Deputados com Maiores Despesas',
                  labels={'NomeDeputado': 'Deputado', 'ValorDocumento': 'Valor Total (R$)'},
                  color='NomeDeputado')
    fig2.update_layout(xaxis_tickangle=45)
    
    # Gráfico 3: Despesas ao longo do tempo
    filtered_df['AnoMes'] = filtered_df['DataDocumento'].dt.to_period('M').astype(str)
    df_tempo = filtered_df.groupby('AnoMes')['ValorDocumento'].sum().reset_index()
    fig3 = px.line(df_tempo, x='AnoMes', y='ValorDocumento',
                   title='Despesas Totais ao Longo do Tempo (Mensal)',
                   labels={'AnoMes': 'Mês/Ano', 'ValorDocumento': 'Valor Total (R$)'})
    
    # Gráfico 4: Despesas por UF
    df_uf = filtered_df.groupby('UF')['ValorDocumento'].sum().reset_index()
    fig4 = px.bar(df_uf, x='UF', y='ValorDocumento',
                  title='Despesas Totais por UF',
                  labels={'UF': 'Unidade Federativa', 'ValorDocumento': 'Valor Total (R$)'},
                  color='UF')
    
    # Gráfico 5: Distribuição dos valores
    fig5 = px.histogram(filtered_df, x='ValorDocumento', nbins=50,
                        title='Distribuição dos Valores das Despesas',
                        labels={'ValorDocumento': 'Valor da Despesa (R$)'},
                        log_y=True)
    
    return fig1, fig2, fig3, fig4, fig5

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8052))
    app.run(debug=False, host='0.0.0.0', port=port)

