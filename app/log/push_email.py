import os
import smtplib as smtp
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv(override=True)

EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_TO = os.getenv('EMAIL_TO')


def enviar_alerta_email(fab: str, erro: str):
    """Envia um alerta por email quando ocorre um erro em uma conexão."""
    assunto = f"[Alerta] Erro no Fabricante {fab}"
    corpo = f"Um erro ocorreu no fabricante {fab}: {erro}"

    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER # type: ignore
    msg['To'] = EMAIL_TO # type: ignore
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        with smtp.SMTP(EMAIL_HOST, EMAIL_PORT) as server: # type: ignore
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS) # type: ignore
            server.send_message(msg)
    except Exception as e:
        print(f"Erro ao enviar email: {e}")


