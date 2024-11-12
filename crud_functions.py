import sqlite3

def initate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
        )
    ''')

    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',('Товар 1', 'Описание товара 1', 100))
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',('Товар 2', 'Описание товара 2', 200))
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',('Товар 3', 'Описание товара 3', 300))
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',('Товар 4', 'Описание товара 4', 400))



def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    conn.close()

    return products



    connection.commit()
    connection.close()