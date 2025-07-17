from mcp.server.fastmcp import FastMCP, Context
from infra.sqlite_connection import SQLiteConnection

# instance the MCP server
mcp = FastMCP("MCP training")
db = SQLiteConnection()

@mcp.tool()
def hello_world(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}! Welcome to MCP SSE Training."

@mcp.tool()
def biggest_sales() -> list:
    """
    Adds a new sale record to the table.
    """
    
    try:
        query = """
        SELECT valor_venda, produto, cliente FROM faturamento_vendas
        ORDER BY valor_venda DESC
        LIMIT 10;
        """
        resultados = db.fetch_all(query=query)
        return resultados
    except Exception as e:
        return f"Error fetching biggest sales: {e}"

@mcp.tool()
def select_database(tabel_name: str, ctx: Context) -> list:
    """
    Selects all records from a specified table.
    """


    query = f"SELECT * FROM {tabel_name};"
    resultados = db.fetch_all(query=query)
    return resultados

@mcp.tool()
def add_sale(produto: str, cliente: str, valor_venda: float) -> str:
    """
    Inserts a new sale record into the faturamento_vendas table.
    """
    
    try:
        query = """
        INSERT INTO faturamento_vendas (produto, cliente, valor_venda)
        VALUES (:produto, :cliente, :valor_venda);
        """
        params = {
            "produto": produto,
            "cliente": cliente,
            "valor_venda": valor_venda
        }
        result = db.execute_query(query=query, params=params)
        if result:
            return "New sale recorded successfully."
    except Exception as e:
        return f"Error recording new sale: {e}"