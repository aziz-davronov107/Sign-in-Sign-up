import sqlite3


def get_connection():
    return sqlite3.connect("data.db")


def create_table():
    db = get_connection()

    cursor  = db.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username  TEXT NOT NULL,
            password INTEGER,
            repeat_password INTEGER,
            email_address TEXT           
        )                   
    ''')

    db.commit()
    cursor.close()

create_table()
