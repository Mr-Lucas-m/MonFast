from fastapi import FastAPI
from threading import Thread
from fastapi.middleware.cors import CORSMiddleware
from app.log.monitor_remote import iniciar_agendamento
from app.routers.route_resulte import router as status_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Específico para dev
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"]
)

app.on_event("startup")
def start_agendador():
    thread = Thread(target=iniciar_agendamento)
    thread.daemon = True
    thread.start()

@app.get("/statusAgendamento")
def status():
    return {"status": "ok"}


app.include_router(status_router)

@app.on_event("startup")
def start_monitoring():
    thread = Thread(target=iniciar_agendamento)
    thread.daemon = True
    thread.start()





