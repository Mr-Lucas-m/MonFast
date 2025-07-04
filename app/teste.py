from log.monitor_remote import testar_todas_conexoes
from log.push_email import enviar_alerta_email


if __name__ == "__main__":
    enviar_alerta_email("Fab toc", "Erro de conexão")
    help(enviar_alerta_email)