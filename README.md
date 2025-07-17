# MCP Training

Este projeto implementa um servidor MCP (Model Context Protocol) que fornece ferramentas para análise de dados de vendas usando SQLite e integração com client agent-OpenAI.

## 📋 Pré-requisitos

- Python 3.10+
- Node.js (para o inspector MCP)
- SQLite3

## 🚀 Configuração do Projeto

```bash
git clone https://github.com/Leonardojdss/MCP-training-openai.git
cd MCP-training-openai
```

### 1. Configurar Ambiente Virtual

```bash
# Criar e ativar ambiente virtual
python -m venv env
source env/bin/activate  # macOS/Linux
# ou
env\Scripts\activate  # Windows
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar Banco de Dados

```bash
# Criar diretório do banco
mkdir -p database

# Criar tabelas
sqlite3 database/costumer-database.db < dependencias/create_table.sql

# Inserir dados de exemplo
sqlite3 database/costumer-database.db < dependencias/faturamento_vendas_insert.sql
```

### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis (se usar Azure OpenAI):

```env
DATABASE_PATH=path_do_banco_sqlite_criado(exemplo: database/costumer-database.db)
AZURE_OPENAI_API_KEY=sua_chave_api
AZURE_OPENAI_API_VERSION=2023-05-15
AZURE_OPENAI_ENDPOINT=https://seu-endpoint.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=seu-deployment
```

### 5. Configurar PYTHONPATH

```bash
export PYTHONPATH=/Users/leonardojdss/Desktop/projetos/MCP-training-openai
```

## 🏃‍♂️ Executando o Projeto

### Iniciar o Servidor MCP

```bash
cd MCP_server
uvicorn server:mcp_app --host 0.0.0.0 --port 8000
```

### Testar as Ferramentas MCP

```bash
npx @modelcontextprotocol/inspector
```

### Iniciar o Client MCP

```bash
python3 client_local_azure_openai.py http://localhost:8000/sse
```

## 🛠️ Estrutura do Projeto

```
MCP-training-openai/
├── README.md
├── requirements.txt
├── Agent-Client-OpenAI/      # Cliente OpenAI para integração
│   └── client.py
├── database/                 # Banco de dados SQLite
│   └── costumer-database.db
├── dependencias/            # Scripts SQL
│   ├── create_table.sql
│   └── faturamento_vendas_insert.sql
├── MCP_server/              # Servidor MCP
│   ├── server.py
│   ├── capacities/
│   │   └── tools.py         # Ferramentas MCP disponíveis
│   └── infra/
│       └── sqlite_connection.py
└── env/                     # Ambiente virtual
```