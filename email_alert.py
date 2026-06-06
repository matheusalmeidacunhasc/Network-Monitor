import smtplib 
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()


def enviar_alerta(host, status):

    remetente = os.getenv("EMAIL_REMETENTE")
    destinatario = os.getenv("EMAIL_DESTINATARIO")
    senha = os.getenv("EMAIL_SENHA")

    assunto = f"Alerta: {host} está fora!"
    corpo = f"O host {host} foi detectado como fora do ar. \nStatus: {status}"
    
    msg = MIMEText(corpo)
    msg["Subject"] = assunto
    msg["From"] = remetente
    msg["To"] = destinatario

    with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, msg.as_string())
 
        print(f"Alerta enviado para {destinatario}")
