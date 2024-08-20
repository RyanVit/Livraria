import psycopg2
from psycopg2 import sql

def connect():
    conn = psycopg2.connect(
        dbname="livraria",
        user="postgres",
        password="***",  # substitua por sua senha
        host="localhost"
    )
    return conn

def close(conn):
    conn.commit()
    conn.close()
