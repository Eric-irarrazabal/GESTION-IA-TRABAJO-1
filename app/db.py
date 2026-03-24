import psycopg2
from psycopg2.extras import RealDictCursor
from flask import current_app


def get_connection():
    database_url = current_app.config["DATABASE_URL"]

    if not database_url:
        raise ValueError("DATABASE_URL no está configurada")

    return psycopg2.connect(database_url, cursor_factory=RealDictCursor)


def test_database_connection():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT NOW() AS server_time;")
            return cursor.fetchone()
    finally:
        conn.close()


def get_all_products():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT id, nombre, precio, stock
                FROM productos
                ORDER BY id;
            """)
            return cursor.fetchall()
    finally:
        conn.close()