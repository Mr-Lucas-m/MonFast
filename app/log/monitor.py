import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def testar_postgres():
    host = os.getenv("CONN3_HOST")
    port = os.getenv("CONN3_PORT")
    database = os.getenv("CONN3_DB")
    user = os.getenv("CONN3_USER")
    password = os.getenv("CONN3_PASS")

    try:
        conn = pyodbc.connect(
            f"DRIVER={{PostgreSQL Unicode(x64)}};"
            f"SERVER={host};PORT={port};DATABASE={database};UID={user};PWD={password};",
            timeout=5
        )
        conn.close()
        print("✅ Conexão PostgreSQL bem-sucedida!")
    except Exception as e:
        print(f"❌ Erro ao conectar no PostgreSQL: {e}")

testar_postgres()
    

# import pyodbc

# def testar_odbc(dsn: str) -> bool:
#     try:
#         conn = pyodbc.connect(f"DSN={dsn};", timeout=5)
#         conn.close()
#         print(f"Conexão {dsn} funcionando!")
#         return True
#     except Exception as e:
#         print(f"Erro na conexão ODBC {dsn}: {e}")
#         return False

# if __name__ == "__main__":
#     testar_odbc("MONFAST_PG")  # Use o nome que você deu no Data Source