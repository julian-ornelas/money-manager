import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('financial_database.db')
cursor = conn.cursor()

# Create tables if they don't exist to database file
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        name TEXT,
        amount REAL NOT NULL,
        category_id INTEGER,
        description TEXT,
        date DATE,
        timestamp_created DATETIME,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()