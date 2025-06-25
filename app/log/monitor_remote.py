import os
from dotenv import load_dotenv
import schedule
import time
import threading

from resultado.status import resultados_conexoes

# FAB-SIZA
def testar_sql_server_fab_siza(fab ,host, db, user, pwd, port):
    import pyodbc
    try:
        conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={host},{port};"
            f"DATABASE={db};"
            f"UID={user};"
            f"PWD={pwd};"
            "Encrypt=no;"
            "TrustServerCertificate=yes;",
            timeout=5
        )
        conn.close()
        print(f"[✓] FAB-SIZA OK: {host}")
        resultados_conexoes[fab] = {"status": "OK", "host": host}
    except Exception as e:
        print(f"[X] FAB-SIZA ERRO: {host} - {e}")
        resultados_conexoes[fab] = {"status": "ERRO", "host": host, "erro": e}

# FAB-MA
def testar_sql_server_fab_ma(fab ,host, db, user, pwd, port):
    import pyodbc
    try:
        conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={host},{port};"
            f"DATABASE={db};"
            f"UID={user};"
            f"PWD={pwd};"
            "Encrypt=no;"
            "TrustServerCertificate=yes;",
            timeout=5
        )
        conn.close()
        print(f"[✓] FAB-MA OK: {host}")
        resultados_conexoes[fab] = {"status": "OK", "host": host}
    except Exception as e:
        print(f"[X] FAB-MA ERRO: {host} - {e}")
        resultados_conexoes[fab] = {"status": "ERRO", "host": host, "erro": e}

# FAB-PARAISO
def testar_sql_server_fab_paraiso(fab ,host, db, user, pwd, port):
    import pyodbc
    try:
        conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={host},{port};"
            f"DATABASE={db};"
            f"UID={user};"
            f"PWD={pwd};"
            "Encrypt=no;"
            "TrustServerCertificate=yes;",
            timeout=5
        )
        conn.close()
        print(f"[✓] FAB-PARAISO OK: {host}")
        resultados_conexoes[fab] = {"status": "OK", "host": host}
    except Exception as e:
        print(f"[X] FAB-PARAISO ERRO: {host} - {e}")
        resultados_conexoes[fab] = {"status": "ERRO", "host": host, "erro": e}

# FAB-ARAG
def testar_sql_server_fab_arag(fab ,host, db, user, pwd, port):
    import pyodbc
    try:
        conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={host},{port};"
            f"DATABASE={db};"
            f"UID={user};"
            f"PWD={pwd};"
            "Encrypt=no;"
            "TrustServerCertificate=yes;",
            timeout=5
        )
        conn.close()
        print(f"[✓] FAB-ARAG OK: {host}")
        resultados_conexoes[fab] = {"status": "OK", "host": host}
    except Exception as e:
        print(f"[X] FAB-ARAG ERRO: {host} - {e}")
        resultados_conexoes[fab] = {"status": "ERRO", "host": host, "erro": e}

# FAB-SANTAREM
def testar_sql_server_fab_santarem(fab ,host, db, user, pwd, port):
    import pyodbc
    try:
        conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={host},{port};"
            f"DATABASE={db};"
            f"UID={user};"
            f"PWD={pwd};"
            "Encrypt=no;"
            "TrustServerCertificate=yes;",
            timeout=5
        )
        conn.close()
        print(f"[✓] FAB-SANTAREM OK: {host}")
        resultados_conexoes[fab] = {"status": "OK", "host": host}
    except Exception as e:
        print(f"[X] FAB-SANTAREM ERRO: {host} - {e}")
        resultados_conexoes[fab] = {"status": "ERRO", "host": host, "erro": e}

# FAB-TOC
def testar_sql_server_fab_toc(fab ,host, db, user, pwd, port):
    import pyodbc
    try:
        conn = pyodbc.connect(
            f"DRIVER={{SQL Server}};"
            f"SERVER={host},{port};"
            f"DATABASE={db};"
            f"UID={user};"
            f"PWD={pwd};"
            "Encrypt=no;"
            "TrustServerCertificate=yes;",
            timeout=5
        )
        conn.close()
        print(f"[✓] FAB-TOC OK: {host}")
        resultados_conexoes[fab] = {"status": "OK", "host": host}
    except Exception as e:
        print(f"[X] FAB-TOC ERRO: {host} - {e}")
        resultados_conexoes[fab] = {"status": "ERRO", "host": host, "erro": e}

# Testar todas as conexões usando .env
def testar_todas_conexoes():
    print("🔁 Iniciando teste de conexões...")
    load_dotenv()
    total = int(os.getenv("TOTAL_CONEXOES", 0))

    if total == 0:
        print("⚠️ TOTAL_CONEXOES não definido no .env")
        return

    for i in range(1, total + 1):
        tipo = os.getenv(f"CONN{i}_TIPO")
        fab = os.getenv(f"CONN{i}_FAB")
        host = os.getenv(f"CONN{i}_HOST")
        port = os.getenv(f"CONN{i}_PORT")
        db   = os.getenv(f"CONN{i}_DB")
        user = os.getenv(f"CONN{i}_USER")
        pwd  = os.getenv(f"CONN{i}_PASS")
        if not all([tipo, fab, host, port, db, user, pwd]):
            print(f"⚠️ Dados incompletos em CONN{i}, pulando...")
            continue
        fab_upp = fab.upper()

        if fab_upp == 'FAB-TOC':
            testar_sql_server_fab_toc(fab ,host, db, user, pwd, port)
        elif fab_upp == 'FAB-MA':
            testar_sql_server_fab_ma(fab ,host, db, user, pwd, port)
        elif fab_upp == 'FAB-PARAISO':
            testar_sql_server_fab_paraiso(fab ,host, db, user, pwd, port)
        elif fab_upp == 'FAB-SIZA':
            testar_sql_server_fab_siza(fab ,host, db, user, pwd, port)
        elif fab_upp == 'FAB-ARAG':
            testar_sql_server_fab_arag(fab ,host, db, user, pwd, port)
        elif fab_upp == 'FAB-SANTAREM':
            testar_sql_server_fab_santarem(fab ,host, db, user, pwd, port)
        else:
            print(f"[!] FAB de conexão não encontrada: {fab}")

# Agendamento com schedule
def iniciar_agendamento():
    schedule.every(1).minutes.do(testar_todas_conexoes)
    testar_todas_conexoes()  # Primeiro teste imediato
    while True:
        schedule.run_pending()
        time.sleep(1)
