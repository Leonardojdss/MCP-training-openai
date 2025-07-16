Iniciar servidor MCP - uvicorn server:mcp_app --host 0.0.0.0 --port 8000

testar ferramentas MCP - npx @modelcontextprotocol/inspector

## Criar e popular o banco de dados

// criar pasta do banco
mkdir -p database

# Criar o banco de dados
sqlite3 database/costumer-database.db < dependencias/create_table.sql

# Inserir dados de exemplo
sqlite3 database/costumer-database.db < dependencias/faturamento_vendas_insert.sql
