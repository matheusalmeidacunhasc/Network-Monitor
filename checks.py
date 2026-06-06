import subprocess
import requests
def verificar_ping(host):
    resultado = subprocess.run(
        ["ping", "-c", "1", host], 
        capture_output=True
    )

    return resultado.returncode == 0

def verificar_http(url):

    try:

        resposta = requests.get(

            url,
            timeout=5

        )

        return resposta.status_code

    except:
        return None
