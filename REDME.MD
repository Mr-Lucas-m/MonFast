# ESTRUTURA BASICA DO PROJETO

    MONFAST/
│
├── app/
│   ├── db/
│   │   ├── connection.py         ← Conexão com o PostgreSQL via SQLAlchemy
│   │   └── 
│   │
│   ├── Services/
│   │   ├──         ← (LOGICA DE NEGOCIO CRUD)
│   │   └── 
│   │
│   ├── log/
│   │   ├── monitor.py            ← Monitoramento contínuo dos IPs (ping, logs)
│   │   └── 
│   │
│   ├── model/
│   │   ├── models.py             ← Modelos SQLAlchemy (Filial, Conexao, Log)
│   │   └── y
│   │
│   ├── routers/
│   │   ├── route.py              ← Rotas de API (GET/POST de conexões, filiais, logs)
│   │   └──
│   │
│   ├── schema/
│   │   ├── filial_schem.py            ← Schemas do Pydantic (Entrada/Saída da API)
│   │   ├── conexao_schem.py
│   │   ├── log_schem.py
|   |   └── relatorio_schem.py
│   │
│   ├── core/
│   │   ├── config.py             ← Carrega variáveis de ambiente (.env)
│   │   └── 
│
├── .env                          ← Variáveis do PostgreSQL (DATABASE_URL etc.)
├── requirements.txt              ← Dependências do projeto
├── main.py                       ← Inicialização do FastAPI + inclusão de rotas
└── README.md                     ← (Opcional) Documentação do projeto
