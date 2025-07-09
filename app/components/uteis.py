from datetime import datetime, timedelta

# TEMPORIZADOR PARA ENVIO

ultimo_alerta = {}
INTERVALO_MINUTOS = 10
def pode_enviar_alerta(fab: str):
    """
    Verifica se pode enviar um alerta para o responsavel a cada intervalo de tempo.
    """
    agora = datetime.now()
    ultimo = ultimo_alerta.get(fab)
    if not ultimo or agora - ultimo > timedelta(minutes=INTERVALO_MINUTOS):
        ultimo_alerta[fab] = agora
        return True
    return False