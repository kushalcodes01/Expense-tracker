import sqlite3

DB_NAME = "expense.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL)
    """)

    conn.commit()
    conn.close()

def add_expense(title, amount, category, date):
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses(title, amount, category, date)
        values (?,?,?,?)""",
        (title, amount, category, date)
    )
    conn.commit()
    conn.close()

def get_all_expenses():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses=cursor.fetchall()

    conn.close()
    return expenses

