import sqlite3

from app.config import get_db_path


def get_connection():
    return sqlite3.connect(get_db_path())


def get_schema():
    return """
customers(id, name, city, country)
products(id, name, category, unit_price)
orders(id, customer_id, order_date, total_amount)
"""


def run_query(sql: str):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    columns = [item[0] for item in cursor.description]
    connection.close()
    return columns, rows
