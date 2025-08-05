# Dashboard de Despesas dos Deputados Federais

Este projeto desenvolve um sistema completo de análise de dados que consome informações da API pública da Câmara dos Deputados do Brasil, realiza análise exploratória de dados (EDA) e apresenta os resultados através de um dashboard web interativo.

## 📋 Descrição do Projeto

O sistema coleta dados de despesas parlamentares através da API de Dados Abertos da Câmara dos Deputados, processa e limpa essas informações, realiza análises exploratórias e apresenta os resultados em um dashboard web interativo construído com Dash e Plotly.

### Funcionalidades Principais

- **Coleta de Dados**: Ingestão automatizada de dados da API da Câmara dos Deputados
- **Processamento**: Limpeza e tratamento dos dados coletados
- **Análise Exploratória**: Geração de insights através de visualizações
- **Dashboard Interativo**: Interface web com filtros dinâmicos por data e categoria
- **Deploy Ready**: Configurado para deploy em plataformas como Render

## 🏗️ Arquitetura do Projeto

```
├── data/
│   ├── raw/                    # Dados brutos da API
│   └── processed/              # Dados processados e limpos
├── src/
│   ├── ingestion/              # Módulo de coleta de dados
│   │   └── data_ingestion.py
│   ├── processing/             # Módulo de processamento
│   │   └── data_processing.py
│   ├── analysis/               # Módulo de análise exploratória
│   │   └── eda.py
│   └── dashboard/              # Dashboard web
│       └── app.py
├── requirements.txt            # Dependências do projeto
├── Procfile                   # Configuração para deploy
├── runtime.txt                # Versão do Python
└── README.md                  # Documentação
```

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.11+
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd dashboard-deputados
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Execução Local

1. **Coleta de Dados**:
```bash
python src/ingestion/data_ingestion.py
```

2. **Processamento dos Dados**:
```bash
python src/processing/data_processing.py
```

3. **Análise Exploratória** (opcional):
```bash
python src/analysis/eda.py
```

4. **Dashboard**:
```bash
python src/dashboard/app.py
```

O dashboard estará disponível em `http://localhost:8052`

## 📊 Funcionalidades do Dashboard

O dashboard apresenta 5 visualizações principais:

1. **Despesas por Tipo**: Gráfico de barras mostrando o total gasto por categoria de despesa
2. **Top 10 Deputados**: Ranking dos deputados com maiores gastos
3. **Evolução Temporal**: Linha do tempo mostrando a evolução das despesas mensais
4. **Despesas por UF**: Distribuição geográfica dos gastos
5. **Distribuição de Valores**: Histograma da distribuição dos valores das despesas

### Filtros Disponíveis

- **Filtro por Data**: Seleção de período específico através de date picker
- **Filtro por Tipo de Despesa**: Seleção múltipla de categorias de despesas

## 🔧 Tecnologias Utilizadas

- **Python 3.11**: Linguagem principal
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Visualizações interativas
- **Dash**: Framework para dashboard web
- **Requests**: Consumo da API REST

## 📡 API Utilizada

O projeto consome dados da [API de Dados Abertos da Câmara dos Deputados](https://dadosabertos.camara.leg.br/swagger/api.html), especificamente:

- **Endpoint de Deputados**: `/deputados` - Lista de deputados
- **Endpoint de Despesas**: `/deputados/{id}/despesas` - Despesas por deputado

## 🚀 Deploy

### Render

O projeto está configurado para deploy no Render:

1. Conecte seu repositório ao Render
2. Configure como Web Service
3. Use as configurações:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python src/dashboard/app.py`

### Outras Plataformas

Para outras plataformas, certifique-se de:
- Instalar as dependências do `requirements.txt`
- Configurar a variável de ambiente `PORT` se necessário
- Executar `python src/dashboard/app.py`

## 📈 Análises Disponíveis

O sistema fornece insights sobre:

- Distribuição de gastos por categoria de despesa
- Ranking de deputados por volume de gastos
- Tendências temporais de despesas
- Distribuição geográfica por estado
- Padrões de distribuição de valores

## 🤝 Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Contato

Para dúvidas ou sugestões, entre em contato através dos issues do GitHub.

---

**Nota**: Este projeto foi desenvolvido para fins educacionais e de transparência pública, utilizando dados oficiais disponibilizados pela Câmara dos Deputados do Brasil.

