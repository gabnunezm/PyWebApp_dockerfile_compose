from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Configuración de la base de datos
DB_HOST = os.getenv('DB_HOST', 'db')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'rootpassword')
DB_NAME = os.getenv('DB_NAME', 'testdb')

def connect_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/')
def hello():
    conn = connect_db()
    if conn:
        return "¡Hola Mundo! Conexión a MySQL exitosa."
    else:
        return "Error al conectar a la base de datos."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)