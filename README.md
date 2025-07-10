# MonFast

Sistema de **monitoramento remoto de conexões com bancos de dados**, inicialmente aplicado a unidades FAB (como TOC, SIZA, STM etc.), com **alertas automáticos por e-mail e WhatsApp** em caso de falha de conexão.\
O projeto foi desenvolvido por **Lucas Marques** durante o estágio no Frango Americano, visando garantir maior confiabilidade nos sistemas distribuídos entre as filiais.

> A estrutura do sistema é flexível e **pode ser facilmente adaptada a diferentes empresas, serviços, tipos de banco de dados ou critérios de alerta**, conforme a necessidade de cada cliente.

---

## 🛠️ Funcionalidades

- **Monitoramento de bancos SQL Server e MySQL**
- **Agendamento automático com **``
- **Envio de alertas por e-mail via Gmail SMTP**
- **Envio de alertas via WhatsApp com Twilio**
- **Controle de tempo entre alertas (evita spam)**
- **Variáveis de ambiente centralizadas no **``
- **API REST integrada com FastAPI**
- **Estrutura modularizada para fácil expansão**

---

## ⚙️ Instalação e Execução

### Clonando o projeto

```bash
git clone https://github.com/seu_usuario/monfast-backend.git
cd monfast
pip install -r requirements.txt
```

### Executando o monitoramento (modo contínuo)

```bash
python -m app.log.monitor_remote
```

### Executando testes manuais

```bash
python teste.py
```

---

## 🔁 Exemplo de .env

```env

# Conexão SQL Server
CONN1_TIPO=sqlserver
CONN1_FAB=FAB-TOC
CONN1_HOST=177.130.49.56
CONN1_PORT=1433
CONN1_DB=MeuBanco
CONN1_USER=usuario_sql
CONN1_PASS=senha_sql

# Conexão MySQL
CONN2_TIPO=mysql
CONN2_FAB=FAB-STM
CONN2_HOST=177.133.94.59
CONN2_PORT=51434
CONN2_DB=uebis_stm
CONN2_USER=usuario_mysql
CONN2_PASS=senha_mysql

# Número total de conexões definidas
TOTAL_CONEXOES=3

# E-mail
EMAIL_ORIGEM=seu_email@gmail.com
EMAIL_SENHA=senha_app_google
EMAIL_DESTINO=destinatario@email.com

# WhatsApp via Twilio
TWILIO_SID=...
TWILIO_TOKEN=...
TWILIO_PHONE=whatsapp:+1415...
DESTINO_WHATSAPP=whatsapp:+55SEUNUMERO
```

---

## 📦 Estrutura do Projeto

```bash
MONFAST/
️
├── app/
│   ├── components/
│   │   └── uteis.py                # Funções auxiliares gerais
│   │
│   ├── Services/
│   │   └── relatorio_crud.py      # Lógica de CRUDs para relatórios (em desenvolvimento)
│   │
│   ├── log/
│   │   ├── monitor_remote.py      # Agendamento e verificação das conexões
│   │   ├── push_email.py          # Alerta via e-mail (SMTP)
│   │   └── push_whatsapp.py       # Alerta via WhatsApp (Twilio)
│   │
│   ├── routers/
│   │   └── route_resulte.py       # Rotas de API para consulta das conexões
│   │
│   ├── resultado/
│   │   └── status.py              # Armazenamento dos resultados (cache temporário)
│   │
│   ├── core/
│   │   └── config.py              # Carrega variáveis do .env
│   │
│   └── main.py                    # Inicialização do FastAPI
️
├── .env                           # Configuração dos bancos, email, WhatsApp
├── requirements.txt               # Bibliotecas necessárias
├── teste.py                       # Script de teste de envio
└── README.md                      # Documentação do projeto
```

---

## 🚀 Tecnologias

- **Python 3.10+**
- **FastAPI** – API web leve e rápida
- **PyODBC** – Conexão com SQL Server
- **mysql-connector-python** – Conexão com MySQL
- **Schedule** – Agendamento de tarefas
- **dotenv** – Carregamento de variáveis de ambiente
- **smtplib / email** – Envio de email com Gmail SMTP
- **Twilio** – Envio de mensagens WhatsApp

---

## 👨‍💼 Contato

- **Lucas Marques**\
  [GitHub](https://github.com/Mr-Lucas-m)\
  [Email](mailto\:ti.lucas.mr@gmail.com)
