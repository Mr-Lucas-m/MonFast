import os
from dotenv import load_dotenv
import schedule
import time

# Banco: PostgreSQL
def testar_postgres(host, db, user, pwd, port):
    import psycopg2
    try:
        conn = psycopg2.connect(host=host, dbname=db, user=user, password=pwd, port=port, connect_timeout=5)
        conn.close()
        print(f"[✓] PostgreSQL OK: {host}")
    except Exception as e:
        print(f"[X] PostgreSQL ERRO: {host} - {e}")

# Banco: SQL Server
def testar_sql_server(host, db, user, pwd, port):
    import pyodbc
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={host},{port};DATABASE={db};UID={user};PWD={pwd};Encrypt=no;TrustServerCertificate=yes;",
            timeout=5
        )
        conn.close()
        print(f"[✓] SQL Server OK: {host}")
    except Exception as e:
        print(f"[X] SQL Server ERRO: {host} - {e}")

# Banco: MariaDB
def testar_mariadb(host, db, user, pwd, port):
    import pymysql
    try:
        conn = pymysql.connect(host=host, user=user, password=pwd, database=db, port=int(port), connect_timeout=5)
        conn.close()
        print(f"[✓] MariaDB OK: {host}")
    except Exception as e:
        print(f"[X] MariaDB ERRO: {host} - {e}")

# Carrega .env e testa todas as conexões configuradas
def testar_todas_conexoes():
    load_dotenv()
    total = int(os.getenv("TOTAL_CONEXOES", 0))

    for i in range(1, total + 1):
        tipo = os.getenv(f"CONN{i}_TIPO")
        host = os.getenv(f"CONN{i}_HOST")
        port = os.getenv(f"CONN{i}_PORT")
        db   = os.getenv(f"CONN{i}_DB")
        user = os.getenv(f"CONN{i}_USER")
        pwd  = os.getenv(f"CONN{i}_PASS")

        print(f"--- Testando conexão {i}: {tipo} ({host}) ---")
        if tipo == "postgres":
            testar_postgres(host, db, user, pwd, port)
        elif tipo == "sqlserver":
            testar_sql_server(host, db, user, pwd, port)
        elif tipo == "mariadb":
            testar_mariadb(host, db, user, pwd, port)
        else:
            print(f"[!] Tipo não suportado: {tipo}")

# Agendamento com schedule
schedule.every(1).minutes.do(testar_todas_conexoes)

print("⏱️ Monitoramento iniciado. Pressione Ctrl+C para parar.")
while True:
    schedule.run_pending()
    time.sleep(1)
