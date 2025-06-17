import os
import json
import pyodbc
from dotenv import load_dotenv

load_dotenv()
conexoes = []

total = int(os.getenv("TOTAL_CONEXOES", 0))

for i in range(1, total + 1):
    tipo = os.getenv(f"CONN{i}_TIPO")
    host = os.getenv(f"CONN{i}_HOST")
    port = os.getenv(f"CONN{i}_PORT")
    db   = os.getenv(f"CONN{i}_DB")
    user = os.getenv(f"CONN{i}_USER")
    pwd  = os.getenv(f"CONN{i}_PASS")

    conexoes.append({
        "tipo": tipo,
        "host": host,
        "port": port,
        "db": db,
        "user": user,
        "pwd": pwd
    })
for c in conexoes:
    if c["tipo"] == "sqlserver":
        testar_sql_server(c["host"], c["db"], c["user"], c["pwd"], c["port"])
        print(f"Conexão {c['tipo']} com {c['host']} testada.")
    elif c["tipo"] == "mariadb":
        testar_mariadb(c["host"], c["db"], c["user"], c["pwd"], c["port"])
    elif c["tipo"] == "postgres":
        testar_postgres(c["host"], c["db"], c["user"], c["pwd"], c["port"])
        
        
def testar_sql_server(tipo, ip, db, user, password, porta):
    try:
        # conn = pyodbc.connect(
        #     f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        #     f"SERVER={ip},{porta};"
        #     f"DATABASE={database};"
        #     f"UID={user};"
        #     f"PWD={password};"
        #     "Encrypt=no;"  # ou "yes" dependendo da política de segurança
        #     "TrustServerCertificate=yes;",
        #     timeout=5
        # )
        conn.close()
        print(f"[✓] Conexão OK com {ip}")
        return True
    except Exception as e:
        print(f"[X] Falha em {ip}: {e}")
        return False

# Exemplo de uso
if __name__ == "__main__":
    pass
