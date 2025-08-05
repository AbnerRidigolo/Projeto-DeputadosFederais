
import requests
import pandas as pd
import os
from datetime import datetime

# URL base da API da Câmara dos Deputados
BASE_URL = "https://dadosabertos.camara.leg.br/api/v2"

def get_deputy_details(deputy_id):
    """
    Obtém detalhes de um deputado específico, incluindo a UF.
    """
    url = f"{BASE_URL}/deputados/{deputy_id}"
    response = requests.get(url)
    details = response.json()
    if 'dados' in details and 'siglaUf' in details['dados']:
        return details['dados']['siglaUf']
    return None

def get_deputy_expenses(year, month):
    """
    Coleta dados de despesas de deputados para um dado ano e mês.
    """
    print(f"Coletando despesas para {month}/{year}...")
    params = {
        'ano': year,
        'mes': month,
        'itens': 100  # Número máximo de itens por página
    }
    all_expenses = []
    
    # Primeiro, obter a lista de deputados para iterar sobre eles
    deputies_url = f"{BASE_URL}/deputados"
    response_deputies = requests.get(deputies_url, params={'itens': 100})
    deputies_data = response_deputies.json()
    
    if 'dados' not in deputies_data:
        print("Erro ao obter lista de deputados.")
        return pd.DataFrame()

    for deputy in deputies_data['dados']:
        deputy_id = deputy['id']
        deputy_name = deputy['nome']
        deputy_uf = get_deputy_details(deputy_id) # Obter a UF do deputado
        
        deputy_expenses_url = f"{BASE_URL}/deputados/{deputy_id}/despesas"
        
        response_expenses = requests.get(deputy_expenses_url, params=params)
        expenses_data = response_expenses.json()
        
        if 'dados' in expenses_data:
            for expense in expenses_data['dados']:
                expense['idDeputado'] = deputy_id
                expense['nomeDeputado'] = deputy_name
                expense['siglaUf'] = deputy_uf # Adicionar a UF à despesa
                all_expenses.append(expense)
        else:
            print(f"Nenhuma despesa encontrada para o deputado {deputy_name} ({deputy_id}) em {month}/{year}.")

    if not all_expenses:
        print(f"Nenhum dado de despesa encontrado para {month}/{year}.")
        return pd.DataFrame()

    df = pd.DataFrame(all_expenses)
    return df

def ingest_data(start_year, start_month, end_year, end_month, output_dir="data/raw"):
    """
    Ingere dados de despesas de deputados para um período especificado
    e salva em arquivos CSV.
    """
    os.makedirs(output_dir, exist_ok=True)

    current_date = datetime(start_year, start_month, 1)
    end_date = datetime(end_year, end_month, 1)

    while current_date <= end_date:
        year = current_date.year
        month = current_date.month
        
        df_expenses = get_deputy_expenses(year, month)
        
        if not df_expenses.empty:
            file_name = f"deputy_expenses_{year}_{month:02d}.csv"
            file_path = os.path.join(output_dir, file_name)
            df_expenses.to_csv(file_path, index=False)
            print(f"Dados de {month}/{year} salvos em {file_path}")
        else:
            print(f"Nenhum dado para {month}/{year} para salvar.")
            
        # Avança para o próximo mês
        if month == 12:
            current_date = datetime(year + 1, 1, 1)
        else:
            current_date = datetime(year, month + 1, 1)

if __name__ == "__main__":
    # Exemplo de uso: coletar dados de janeiro a março de 2024
    ingest_data(2024, 1, 2024, 3)


