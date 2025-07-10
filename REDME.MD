# ESTRUTURA BASICA DO PROJETO

    MONFAST/
│
├── app/
│   │
│   ├── components/
│   │   └── uteis.py                        ←  Logicas uteis para o script principal.
│   │
│   │
│   ├── Services/
│   │   ├── relatorio_crud.py (vazio)        ← (LOGICA DE NEGOCIO CRUD)
│   │    
│   │
│   ├── log/
│   │   ├── monitor_remote.py            ← Monitoramento contínuo dos IPs (ping, logs)
│   │   └── push_email.py 
│   │   └── push_whatsapp.py
│   │
│   ├── routers/
│   │   ├── route_resulte.py              ← Rotas de API (GET/POST de conexões, filiais, logs)
│   │   └──
│   │
│   ├── resultado/
│   │   └── status.py              ← Onde armazena os resultados das conexoes em variavel Global.
│   │
│   │
│   ├── core/
│   │   ├── config.py             ← Carrega variáveis de ambiente (.env)
│   │   └── 
│   ├── main.py
├   ├── teste.py
├── .env                          ← Variáveis de banco, email, whatsapp (DATABASE_URL etc.)
├── requirements.txt              ← Dependências do projeto
├── main.py                       ← Inicialização do FastAPI + inclusão de rotas
└── README.md                     ← (Opcional) Documentação do projeto
