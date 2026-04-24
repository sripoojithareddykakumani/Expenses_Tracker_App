import os

# Detect environment
USE_POSTGRES = os.environ.get("DATABASE_URL")


# CONNECTION
def get_connection():
    if USE_POSTGRES:
        import psycopg2
        conn = psycopg2.connect(os.environ.get("DATABASE_URL"))
        return conn
    else:
        import sqlite3
        conn = sqlite3.connect("expenses.db")
        conn.row_factory = sqlite3.Row
        return conn


# CURSOR 
def get_cursor(conn):
    if USE_POSTGRES:
        import psycopg2.extras
        return conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    else:
        return conn.cursor()


# CREATE TABLES
def create_table():
    conn = get_connection()
    cursor = get_cursor(conn)

    if USE_POSTGRES:
        # PostgreSQL schema
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            amount FLOAT,
            category TEXT,
            date DATE,
            note TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY,
            amount FLOAT
        )
        """)

    else:
        # SQLite schema
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            date TEXT,
            note TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS budget (
            id INTEGER PRIMARY KEY,
            amount REAL
        )
        """)

    conn.commit()
    conn.close()
