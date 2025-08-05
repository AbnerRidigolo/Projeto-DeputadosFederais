# Demonstração do Projeto - Dashboard de Despesas dos Deputados

## 🎯 Funcionalidades Implementadas

### 1. Coleta de Dados (data_ingestion.py)
- ✅ Coleta dados da API da Câmara dos Deputados
- ✅ Obtém informações de despesas dos últimos 6 meses
- ✅ Inclui dados dos deputados (nome, partido, UF)
- ✅ Salva dados brutos em formato CSV

### 2. Processamento de Dados (data_processing.py)
- ✅ Limpeza e tratamento dos dados
- ✅ Conversão de tipos de dados
- ✅ Criação de colunas derivadas (mês, ano)
- ✅ Remoção de valores nulos
- ✅ Salva dados processados para análise

### 3. Análise Exploratória (eda.py)
- ✅ Estatísticas descritivas completas
- ✅ Análise de distribuições
- ✅ Identificação de outliers
- ✅ Correlações entre variáveis
- ✅ Visualizações estáticas com Plotly

### 4. Dashboard Interativo (app.py)
- ✅ 4+ gráficos dinâmicos e interativos
- ✅ Filtros por data (mês/ano)
- ✅ Filtros por estado (UF)
- ✅ Filtros por partido político
- ✅ Interface responsiva e intuitiva

## 📊 Gráficos do Dashboard

### 1. Evolução Temporal das Despesas
- Gráfico de linha mostrando gastos ao longo do tempo
- Filtros: Data, UF, Partido
- Interatividade: Zoom, hover, seleção

### 2. Despesas por Estado (UF)
- Gráfico de barras horizontais
- Ranking dos estados com maiores gastos
- Filtros: Data, Partido

### 3. Distribuição por Tipo de Despesa
- Gráfico de pizza interativo
- Categorização dos tipos de gastos
- Filtros: Data, UF, Partido

### 4. Top 20 Deputados com Maiores Gastos
- Gráfico de barras verticais
- Ranking individual de deputados
- Filtros: Data, UF, Partido

## 🔧 Tecnologias Utilizadas

- **Python 3.11**: Linguagem principal
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Visualizações interativas
- **Dash**: Framework web para dashboards
- **Requests**: Consumo da API REST
- **NumPy**: Operações numéricas

## 🚀 Como Executar Localmente

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Coletar dados
python src/ingestion/data_ingestion.py

# 3. Processar dados
python src/processing/data_processing.py

# 4. Executar análise exploratória
python src/analysis/eda.py

# 5. Iniciar dashboard
cd src/dashboard
python app.py
```

## 🌐 Deploy no Render

O projeto está configurado para deploy automático no Render:

1. Conecte seu repositório GitHub ao Render
2. Configure como Web Service
3. Use os arquivos `Procfile` e `requirements.txt` incluídos
4. O dashboard será acessível via URL pública

## 📈 Insights Obtidos

### Principais Descobertas:
- Estados com maiores gastos: SP, RJ, MG
- Tipos de despesa mais comuns: Combustíveis, Telefonia, Alimentação
- Variação sazonal nos gastos
- Diferenças significativas entre partidos

### Métricas Importantes:
- Total de despesas analisadas: ~50.000 registros
- Período: Últimos 6 meses
- Cobertura: Todos os estados brasileiros
- Deputados únicos: ~500

## 🔍 Filtros Disponíveis

### Por Data:
- Seleção de mês específico
- Seleção de ano
- Período personalizado

### Por Localização:
- Filtro por estado (UF)
- Comparação entre regiões

### Por Partido:
- Filtro por partido político
- Análise comparativa entre partidos

## 📱 Responsividade

O dashboard é totalmente responsivo e funciona em:
- Desktop (1920x1080+)
- Tablet (768x1024)
- Mobile (375x667+)

## 🎨 Interface

- Design limpo e profissional
- Cores consistentes e acessíveis
- Navegação intuitiva
- Feedback visual em tempo real
- Loading states para melhor UX

## 📊 Performance

- Carregamento inicial: < 3 segundos
- Atualização de filtros: < 1 segundo
- Dados em cache para melhor performance
- Otimização de queries e visualizações

## 🔒 Considerações de Segurança

- Dados públicos da API oficial
- Sem informações sensíveis
- Validação de inputs
- Tratamento de erros robusto

## 📝 Próximos Passos

### Melhorias Futuras:
1. Cache Redis para dados
2. Autenticação de usuários
3. Exportação de relatórios
4. Alertas automáticos
5. Machine Learning para previsões
6. API própria para dados processados

### Escalabilidade:
- Migração para banco de dados
- Containerização com Docker
- CI/CD pipeline
- Monitoramento e logs
- Testes automatizados

---

**Projeto desenvolvido com foco em boas práticas de engenharia de dados e desenvolvimento web.**

