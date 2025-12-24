from dotenv import load_dotenv
import os
import mysql.conector


load_dotenv()

def get_connection():
    connection = mysql.conector.connect(
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        name = os.getenv("DB_NAME")
    )
    return connection