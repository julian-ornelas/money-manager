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

cursor.execute('''
    CREATE TABLE IF NOT EXISTS recurring_transactions (
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

def begin():
    paycheck_existance = ("Do you get paid in a frequent manner, like paychecks? (y/n): ")
    if paycheck_existance == "y":
        paycheck = input("How much do you get paid per paycheck?")
        frequency = input("How often? (weekly/biweekly/monthly)")
        pay_date = input("When do you get paid?") # Make this into a calander date select on PyQT