
import pymysql
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def salvar_resultado(host, status):

    conexao = pymysql.connect(
        host="localhost",
        user= os.getenv("DB_USER"),
        password= os.getenv("DB_PASSWORD"),
        database= os.getenv("DB_NAME")
    )
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO monitoramentos (host, status, data_hora) VALUES (%s, %s, %s)",
        (host, status, datetime.now())
    )

    conexao.commit()
    conexao.close()
