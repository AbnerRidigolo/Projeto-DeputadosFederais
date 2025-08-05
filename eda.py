
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

def load_processed_data(input_dir="data/processed"):
    """
    Carrega o DataFrame processado.
    """
    file_path = os.path.join(input_dir, "processed_deputy_expenses.csv")
    if not os.path.exists(file_path):
        print(f"Arquivo {file_path} não encontrado. Execute o processamento de dados primeiro.")
        return pd.DataFrame()
    df = pd.read_csv(file_path)
    # Garantir que a coluna 'DataDocumento' seja do tipo datetime
    df['DataDocumento'] = pd.to_datetime(df['DataDocumento'])
    df['Data'] = pd.to_datetime(df['Data'])
    return df

def generate_eda_plots(df):
    """
    Gera gráficos de análise exploratória de dados usando Plotly.
    Retorna uma lista de figuras Plotly.
    """
    plots = {}

    # 1. Despesas totais por tipo de despesa
    df_tipo_despesa = df.groupby('TipoDespesa')['ValorDocumento'].sum().reset_index()
    fig1 = px.bar(df_tipo_despesa, x='TipoDespesa', y='ValorDocumento',
                  title='Despesas Totais por Tipo de Despesa',
                  labels={'TipoDespesa': 'Tipo de Despesa', 'ValorDocumento': 'Valor Total (R$)'},
                  color='TipoDespesa')
    plots['despesas_por_tipo'] = fig1

    # 2. Despesas totais por deputado (Top 10)
    df_deputado_despesa = df.groupby('NomeDeputado')['ValorDocumento'].sum().nlargest(10).reset_index()
    fig2 = px.bar(df_deputado_despesa, x='NomeDeputado', y='ValorDocumento',
                  title='Top 10 Deputados com Maiores Despesas',
                  labels={'NomeDeputado': 'Deputado', 'ValorDocumento': 'Valor Total (R$)'},
                  color='NomeDeputado')
    plots['despesas_por_deputado'] = fig2

    # 3. Despesas ao longo do tempo (mensal)
    df['AnoMes'] = df['DataDocumento'].dt.to_period('M').astype(str)
    df_tempo = df.groupby('AnoMes')['ValorDocumento'].sum().reset_index()
    fig3 = px.line(df_tempo, x='AnoMes', y='ValorDocumento',
                   title='Despesas Totais ao Longo do Tempo (Mensal)',
                   labels={'AnoMes': 'Mês/Ano', 'ValorDocumento': 'Valor Total (R$)'})
    plots['despesas_ao_longo_tempo'] = fig3

    # 4. Distribuição dos valores das despesas
    fig4 = px.histogram(df, x='ValorDocumento', nbins=50,
                        title='Distribuição dos Valores das Despesas',
                        labels={'ValorDocumento': 'Valor da Despesa (R$)'},
                        log_y=True) # Usar escala logarítmica para melhor visualização devido à assimetria
    plots['distribuicao_valores'] = fig4

    # 5. Despesas por UF
    df_uf_despesa = df.groupby('UF')['ValorDocumento'].sum().reset_index()
    fig5 = px.bar(df_uf_despesa, x='UF', y='ValorDocumento',
                  title='Despesas Totais por UF',
                  labels={'UF': 'Unidade Federativa', 'ValorDocumento': 'Valor Total (R$)'},
                  color='UF')
    plots['despesas_por_uf'] = fig5

    return plots

if __name__ == "__main__":
    df = load_processed_data()
    if not df.empty:
        eda_plots = generate_eda_plots(df)
        # Para visualizar os gráficos, você pode salvá-los como HTML ou exibi-los
        # Exemplo: salvar o primeiro gráfico como HTML
        # eda_plots['despesas_por_tipo'].write_html("despesas_por_tipo.html")
        print("Gráficos EDA gerados com sucesso.")
    


