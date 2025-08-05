
import pandas as pd
import os

def load_and_process_data(input_dir="data/raw", output_dir="data/processed"):
    """
    Carrega os arquivos CSV de despesas brutas, processa-os e salva
    o DataFrame resultante em um único arquivo CSV.
    """
    all_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith('.csv')]
    
    if not all_files:
        print(f"Nenhum arquivo CSV encontrado em {input_dir}.")
        return pd.DataFrame()

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    df_raw = pd.concat(li, axis=0, ignore_index=True)

    # Renomear colunas para facilitar o uso
    df_raw.rename(columns={
        'ano': 'Ano',
        'mes': 'Mes',
        'tipoDespesa': 'TipoDespesa',
        'valorDocumento': 'ValorDocumento',
        'dataDocumento': 'DataDocumento',
        'nomeDeputado': 'NomeDeputado',
        'siglaPartido': 'Partido',
        'siglaUf': 'UF',
        'idDeputado': 'IDDeputado'
    }, inplace=True)

    # Converter 'DataDocumento' para datetime
    df_raw['DataDocumento'] = pd.to_datetime(df_raw['DataDocumento'], errors='coerce')

    # Remover linhas com datas inválidas (se houver)
    df_processed = df_raw.dropna(subset=['DataDocumento'])

    # Criar coluna 'Data' no formato YYYY-MM-DD para facilitar filtros
    df_processed['Data'] = df_processed['DataDocumento'].dt.date

    # Preencher valores nulos em colunas categóricas, se houver
    for col in ['TipoDespesa', 'NomeDeputado', 'Partido', 'UF']:
        if col in df_processed.columns:
            df_processed[col] = df_processed[col].fillna('Desconhecido')

    # Remover duplicatas, se houver
    df_processed.drop_duplicates(inplace=True)

    # Garantir que 'ValorDocumento' é numérico
    df_processed['ValorDocumento'] = pd.to_numeric(df_processed['ValorDocumento'], errors='coerce')
    df_processed = df_processed.dropna(subset=['ValorDocumento'])

    # Criar diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    # Salvar o DataFrame processado
    output_path = os.path.join(output_dir, "processed_deputy_expenses.csv")
    df_processed.to_csv(output_path, index=False)
    print(f"Dados processados salvos em {output_path}")
    
    return df_processed

if __name__ == "__main__":
    df_processed = load_and_process_data()
    print(df_processed.head())
    print(df_processed.info())


