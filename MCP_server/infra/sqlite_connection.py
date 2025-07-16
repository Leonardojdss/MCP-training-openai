from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine, Connection
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

load_dotenv()


class SQLiteConnection:
    def __init__(self):
        db_path = os.getenv("DATABASE_PATH")
        if not db_path or db_path == None:
            raise ValueError("DATABASE_PATH não definida no .env ou valor inválido.")
        self.db_path = db_path
        self.engine: Engine = create_engine(f'sqlite:///{self.db_path}', echo=False, future=True)
        self.conn: Connection | None = None

    def connect(self):
        try:
            self.conn = self.engine.connect()
            return self.conn
        except SQLAlchemyError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def execute_query(self, query: str, params: dict = None):
        if not self.conn:
            self.connect()
        try:
            if params is None:
                params = {}
            result = self.conn.execute(text(query), params)
            self.conn.commit()
            return result
        except SQLAlchemyError as e:
            print(f"Erro ao executar query: {e}")
            return None

    def fetch_all(self, query: str, params: dict = None):
        result = self.execute_query(query, params)
        if result:
            return result.fetchall()
        return []
    
    def test_connection(self) -> bool:
        """
        Testa se a conexão com o banco de dados pode ser estabelecida e executa uma query simples.
        """
        try:
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return True
        except SQLAlchemyError as e:
            print(f"Falha no teste de conexão: {e}")
            return False
        
# # teste de conexão
# if __name__ == "__main__":
#     db = SQLiteConnection()
#     if db.test_connection():
#         print("Conexão com o banco de dados estabelecida com sucesso.")
#     else:
#         print("Falha ao conectar ao banco de dados.")

# # teste de execução de query
#     query = "SELECT * FROM faturamento_vendas;"
#     resultados = db.fetch_all(query=query)
#     print(resultados)