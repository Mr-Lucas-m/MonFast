import pyodbc

def testar_odbc(dsn: str) -> bool:
    try:
        conn = pyodbc.connect(f"DSN={dsn};", timeout=5)
        conn.close()
        print(f"Conexão {dsn} funcionando!")
        return True
    except Exception as e:
        print(f"Erro na conexão ODBC {dsn}: {e}")
        return False

if __name__ == "__main__":
    testar_odbc("MONFAST_PG")  # Use o nome que você deu no Data Source