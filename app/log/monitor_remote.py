import pyodbc

def testar_sql_server(ip, database, user, password, port=1433):
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={ip},{port};"
            f"DATABASE={database};"
            f"UID={user};"
            f"PWD={password};"
            "Encrypt=no;"  # ou "yes" dependendo da política de segurança
            "TrustServerCertificate=yes;",
            timeout=5
        )
        conn.close()
        print(f"[✓] Conexão OK com {ip}")
        return True
    except Exception as e:
        print(f"[X] Falha em {ip}: {e}")
        return False

# Exemplo de uso
testar_sql_server("192.168.0.10", "MinhaBase", "usuario_sql", "senha_segura")
