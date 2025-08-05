# 📊 Dashboard de Despesas dos Deputados Federais

Este projeto é um sistema completo de **engenharia de dados com visualização interativa**, que coleta, processa e analisa os dados públicos das despesas dos deputados federais do Brasil, disponibilizados pela API da Câmara dos Deputados. O objetivo é promover **transparência pública** e **insights analíticos acessíveis** por meio de um **dashboard web**.

---

## 🚀 Funcionalidades

✅ Coleta automatizada de dados diretamente da API da Câmara  
✅ Processamento, limpeza e padronização dos dados  
✅ Análises exploratórias com visualizações interativas  
✅ Dashboard web com filtros por data e tipo de despesa  
✅ Pronto para deploy em plataformas como Render ou Heroku  

---

## 🏗️ Arquitetura do Projeto

```
├── data/
│   ├── raw/                    # Dados brutos da API
│   └── processed/              # Dados tratados para visualização
├── src/
│   ├── ingestion/              # Módulo de coleta de dados (data_ingestion.py)
│   ├── processing/             # Módulo de limpeza e tratamento (data_processing.py)
│   ├── analysis/               # Módulo de análise exploratória (eda.py)
│   └── dashboard/              # Dashboard interativo com Dash (app.py)
├── requirements.txt            # Dependências do projeto
├── Procfile                    # Configuração para deploy (Render/Heroku)
├── runtime.txt                 # Versão do Python
└── README.md                   # Documentação do projeto
```

---

## 📥 Como Executar Localmente

### Pré-requisitos
- Python 3.11+
- pip instalado

### Passos:

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/dashboard-deputados.git
cd dashboard-deputados
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Coleta de dados:
```bash
python src/ingestion/data_ingestion.py
```

4. Processamento dos dados:
```bash
python src/processing/data_processing.py
```

5. Análise exploratória (opcional):
```bash
python src/analysis/eda.py
```

6. Execute o dashboard:
```bash
python src/dashboard/app.py
```

Acesse o dashboard em: [http://localhost:8052](http://localhost:8052)

---

## 📊 O Que o Dashboard Mostra

1. **Despesas por Tipo**  
2. **Top 10 Deputados com Maiores Gastos**  
3. **Evolução Mensal das Despesas**  
4. **Despesas por Estado (UF)**  
5. **Distribuição de Valores**

Filtros:
- Por intervalo de datas
- Por categoria de despesa

---

## ☁️ Deploy no Render (Gratuito)

1. Suba o projeto no GitHub  
2. Acesse [https://render.com](https://render.com)  
3. Crie um Web Service com as configurações:

```
Build Command: pip install -r requirements.txt
Start Command: python src/dashboard/app.py
```

Não é necessário configurar variáveis de ambiente para o funcionamento básico.

---

## 📦 Tecnologias Utilizadas

- Python 3.11  
- Pandas  
- Plotly  
- Dash  
- Requests  
- NumPy  
- HTML/CSS (via Dash)

---

## 📚 Fonte dos Dados

- [API de Dados Abertos da Câmara dos Deputados](https://dadosabertos.camara.leg.br/swagger/api.html)

---

## 📈 Possíveis Extensões

- Filtro por partido e estado (UF)  
- Exportação de relatórios em PDF/Excel  
- Integração com banco de dados (PostgreSQL)  
- Machine Learning para prever tendências de gasto  
- API própria para fornecer os dados tratados

---

## 🛡️ Licença

Este projeto é open-source e distribuído sob a licença MIT.

---

## 🙋‍♂️ Contribua

Contribuições são bem-vindas!  
Basta fazer um fork, criar uma branch e abrir um pull request com suas melhorias.

---

## ✉️ Contato

Dúvidas ou sugestões?  
Abra uma [issue no GitHub](https://github.com/seu-usuario/dashboard-deputados/issues).