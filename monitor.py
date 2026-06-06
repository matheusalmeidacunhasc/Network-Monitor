import yaml
import time
 
from checks import verificar_ping, verificar_http
from database import salvar_resultado
from email_alert import enviar_alerta


with open("hosts.yaml", "r") as arquivo:
    dados = yaml.safe_load(arquivo)
while True:
    for host in dados["hosts"]:

        if host["tipo"] == "ping":
            resultado = verificar_ping(host["endereco"])
        elif host ["tipo"] == "http":
            resultado = verificar_http(host["endereco"])

        print(f"{host['nome']} -> {resultado}")
        salvar_resultado(host["nome"], str(resultado))
        if resultado == False or resultado is None:
            enviar_alerta(f"{host['nome']}", str(resultado))

    time.sleep(300)
