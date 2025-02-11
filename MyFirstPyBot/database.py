import sqlite3
from config import DB_PATH

def db_execute(query, params=()):
    try:
        with sqlite3.connect(DB_PATH, check_same_thread=False) as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()
    except sqlite3.Error as e:
        print(f"Ошибка БД: {e}")

def db_fetchall(query, params=()):
    try:
        with sqlite3.connect(DB_PATH, check_same_thread=False) as conn:
            conn.execute("PRAGMA foreign_keys = ON")
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchall()
    except sqlite3.Error as e:
        print(f"Ошибка БД: {e}")
        return []

# def db_setup():
    # db_execute("""
    # CREATE TABLE IF NOT EXISTS Adds (
    #     Id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     ChatID INTEGER,
    #     Task TEXT,
    #     CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
    # )
    # """)

    # db_execute("""
    # CREATE TABLE IF NOT EXISTS Reminders (
    #     Id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     TaskID INTEGER,
    #     ReminderTime DATETIME,
    #     FOREIGN KEY (TaskID) REFERENCES Adds(Id) ON DELETE CASCADE
    # )
    # """)

def db_setup():
    db_execute("""
    CREATE TABLE IF NOT EXISTS Adds (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        ChatID INTEGER NOT NULL,  
        Task TEXT NOT NULL 
    )
    """)
    db_execute("""
    CREATE TABLE IF NOT EXISTS Reminders (
        Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        TaskID INTEGER NOT NULL,
        ReminderTime TEXT NOT NULL, 
        FOREIGN KEY (TaskID) REFERENCES Adds(Id)
    )
    """)