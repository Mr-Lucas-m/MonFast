import os 
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")
twilio_from = os.getenv("TWILIO_FROM")
twilio_to = os.getenv("TWILIO_TO")

client = Client(account_sid, auth_token)

def enviar_alerta_whatsapp(msg: str):
    messagem = client.messages.create(
        from_=twilio_from,
        to=twilio_to, # type: ignore
        body=msg,
    )
    return messagem.sid


if __name__ == "__main__":
    msg = "AAAAAAAAAAAAATOOPP"
    try:
        enviar_alerta_whatsapp(msg)
        print(f"Mensagem enviada com sucesso: {msg}")
    except Exception as e:
        print(f"Erro ao enviar mensagem via WhatsApp: {e}")
        
        
        
