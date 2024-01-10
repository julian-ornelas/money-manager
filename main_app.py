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

# Commit changes and close connection
conn.commit()
conn.close()