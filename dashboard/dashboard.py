from flask import Flask, render_template
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

def buscar_resultados():
    conexao = pymysql.connect(
        host = "localhost",
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_NAME")
    )
    cursor = conexao.cursor()
    cursor.execute("SELECT host, status, data_hora FROM monitoramentos ORDER BY data_hora DESC LIMIT 50")
    resultados = cursor.fetchall()
    conexao.close()
    return resultados

@app.route("/")
def index():
    resultados = buscar_resultados()
    return render_template("index.html", resultados=resultados)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
