# Instruções Detalhadas para Deploy

Este documento fornece instruções passo a passo para fazer o deploy do Dashboard de Despesas dos Deputados Federais em diferentes plataformas.

## 🚀 Deploy no Render (Recomendado)

O Render é uma plataforma de cloud computing que oferece deploy gratuito para aplicações web.

### Pré-requisitos
- Conta no GitHub
- Conta no Render (gratuita)
- Repositório do projeto no GitHub

### Passo a Passo

1. **Preparar o Repositório**
   ```bash
   # Certifique-se de que todos os arquivos estão commitados
   git add .
   git commit -m "Preparar para deploy"
   git push origin main
   ```

2. **Acessar o Render**
   - Acesse [render.com](https://render.com)
   - Faça login com sua conta GitHub

3. **Criar Novo Web Service**
   - Clique em "New +" no dashboard
   - Selecione "Web Service"
   - Conecte seu repositório GitHub

4. **Configurar o Serviço**
   - **Name**: `dashboard-deputados` (ou nome de sua escolha)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python src/dashboard/app.py`
   - **Instance Type**: `Free` (para teste)

5. **Variáveis de Ambiente** (opcional)
   - Não são necessárias para este projeto
   - O Render automaticamente define a variável `PORT`

6. **Deploy**
   - Clique em "Create Web Service"
   - Aguarde o build e deploy (pode levar alguns minutos)
   - Sua aplicação estará disponível na URL fornecida pelo Render

### Troubleshooting Render

**Problema**: Build falha
- **Solução**: Verifique se o `requirements.txt` está correto
- **Comando**: `pip freeze > requirements.txt`

**Problema**: Aplicação não inicia
- **Solução**: Verifique os logs no dashboard do Render
- **Verificar**: Se o arquivo `src/dashboard/app.py` existe

## 🐳 Deploy com Docker (Avançado)

### Dockerfile
Crie um arquivo `Dockerfile` na raiz do projeto:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8052

CMD ["python", "src/dashboard/app.py"]
```

### Comandos Docker
```bash
# Build da imagem
docker build -t dashboard-deputados .

# Executar container
docker run -p 8052:8052 dashboard-deputados
```

## ☁️ Deploy no Heroku

### Pré-requisitos
- Conta no Heroku
- Heroku CLI instalado

### Configuração
1. **Criar aplicação**:
   ```bash
   heroku create dashboard-deputados
   ```

2. **Configurar buildpack**:
   ```bash
   heroku buildpacks:set heroku/python
   ```

3. **Deploy**:
   ```bash
   git push heroku main
   ```

### Arquivo adicional para Heroku
Crie `app.json`:
```json
{
  "name": "Dashboard Deputados",
  "description": "Dashboard de análise de despesas dos deputados federais",
  "repository": "https://github.com/seu-usuario/dashboard-deputados",
  "keywords": ["python", "dash", "plotly", "data-analysis"],
  "env": {
    "PORT": {
      "description": "Port for the application",
      "value": "8052"
    }
  },
  "buildpacks": [
    {
      "url": "heroku/python"
    }
  ]
}
```

## 🌐 Deploy no Vercel

### Configuração
1. **Instalar Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Configurar vercel.json**:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "src/dashboard/app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "src/dashboard/app.py"
       }
     ]
   }
   ```

3. **Deploy**:
   ```bash
   vercel --prod
   ```

## 🔧 Configurações Importantes

### Variáveis de Ambiente
- `PORT`: Porta da aplicação (definida automaticamente pelas plataformas)
- `DEBUG`: Definir como `False` em produção

### Arquivos Necessários
- `requirements.txt`: Dependências Python
- `Procfile`: Comando de inicialização (Render/Heroku)
- `runtime.txt`: Versão do Python (opcional)

### Otimizações para Produção

1. **Desabilitar Debug**:
   ```python
   app.run(debug=False, host='0.0.0.0', port=port)
   ```

2. **Usar Gunicorn** (opcional):
   ```bash
   # Adicionar ao requirements.txt
   gunicorn==20.1.0
   
   # Modificar Procfile
   web: gunicorn --bind 0.0.0.0:$PORT src.dashboard.app:server
   ```

3. **Cache de Dados**:
   - Implementar cache para evitar múltiplas chamadas à API
   - Usar Redis ou cache em memória

## 📊 Monitoramento

### Logs
- **Render**: Dashboard > Logs
- **Heroku**: `heroku logs --tail`
- **Vercel**: Dashboard > Functions > Logs

### Métricas
- Tempo de resposta
- Uso de memória
- Número de requisições

## 🔒 Segurança

### Boas Práticas
1. **Não expor dados sensíveis** nos logs
2. **Usar HTTPS** (automático nas plataformas)
3. **Validar inputs** do usuário
4. **Rate limiting** para API calls

### Headers de Segurança
```python
@app.server.after_request
def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

## 🚨 Troubleshooting Geral

### Problemas Comuns

1. **Erro de Importação**:
   - Verificar estrutura de pastas
   - Verificar `sys.path.append()`

2. **Dados não Carregam**:
   - Verificar se arquivos de dados existem
   - Executar scripts de ingestão e processamento

3. **Gráficos não Aparecem**:
   - Verificar console do browser para erros JavaScript
   - Verificar se Plotly está instalado

4. **Timeout na API**:
   - Implementar retry logic
   - Usar cache para dados já coletados

### Comandos Úteis

```bash
# Verificar dependências
pip check

# Testar localmente
python src/dashboard/app.py

# Verificar logs
tail -f logs/app.log

# Testar requisições
curl -I http://localhost:8052
```

## 📞 Suporte

Para problemas específicos:
1. Verificar logs da plataforma
2. Consultar documentação oficial
3. Abrir issue no repositório GitHub
4. Verificar status das plataformas de deploy

---

**Dica**: Sempre teste localmente antes de fazer deploy e mantenha backups dos dados importantes.

