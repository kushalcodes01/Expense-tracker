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

def get_expense_by_id(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(

        "SELECT * FROM expenses WHERE id=?",
        (expense_id,)
    )
    expense = cursor.fetchone()
    conn.close()

    return expense

def update_expense(expense_id, title, amount, category, date):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE expenses
        SET title=?, amount=?, category=?, date=?
        WHERE id=?
        """,
        (title, amount, category, date,expense_id)
    )

    rows_updated = cursor.rowcount

    conn.commit()
    conn.close()

    return rows_updated


def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )

    rows_deleted = cursor.rowcount

    conn.commit()
    conn.close()

def get_expenses_by_category(category):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses where category =?",
        (category,)
    )

    expenses = cursor.fetchall()

    conn.close()

    return expenses

def get_total_expense():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT SUM(amount) FROM expenses"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0

def get_category_summary():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        """
    )

    summary = cursor.fetchall()
    conn.close()

    return summary

def get_expenses_by_date(date):
    conn=get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE date=?",
        (date,)
    )

    expenses = cursor.fetchall()
    conn.close()

    return expenses

def get_expenses_by_month(month):
    conn = get_connection()
    cursor=conn.cursor()

    month_pattern = month + "%"

    cursor.execute(
        "SELECT * FROM expenses WHERE date LIKE ?",
        (month_pattern,)
    )

    expenses = cursor.fetchall()
    conn.close()

    return expenses

