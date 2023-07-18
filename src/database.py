import os
import sqlite3

# check if the database file exits
def check_database_exists(database_file):
    return os.path.exists(database_file)

# Create the database file
def create_database(database_file):
    if not check_database_exists(database_file):
        conn = create_connection(database_file)
        create_tables(conn)
        close_connection(conn)
        print("Database File Created {0}".format(database_file))
    else:
        print("Database file already exits: {0}".format(database_file))

# Create database tables
def create_tables(conn):
    if conn:
        try:
            cursor = conn.cursor()
            
            # Create portfolio table
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS Portfolio(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                description TEXT
                            );
                        ''')
            
            # Create Stock table
            cursor.execute(''' 
                            CREATE TABLE IF NOT EXISTS Stock(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                symbol TEXT NOT NULL,
                                name TEXT,
                                quantity INTEGER,
                                price REAL,
                                portfolio_id INTEGER, FOREIGN KEY(portfolio_id) REFERENCES Portfolio (id)
                            );
                        ''')
            
            # Create StockPurchase table
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS StockPurchases (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                stock_id INTEGER,
                                quantity INTEGER,
                                price REAL,
                                purchase_date DATE DEFAULT (datetime('now', 'localtime')),
                                FOREIGN KEY (stock_id) REFERENCES Stock (id)
                            );
                        ''')
            
        except sqlite3.Error as e:
            print(e)
    else:
        print("No database connection available.")

# Create a connection to the database
def create_connection(database_file):
    conn = None
    try:
        conn = sqlite3.connect(database_file)
        print("Connected to database: {0}".format(database_file))
        return conn
    except sqlite3.Error as e:
        print(e)
    
    return conn

# close the database connection
def close_connection(conn):
    if conn:
        conn.close()
        print("Database connection closed.")

# Retrieve all portfolio names from the database
def get_portfolio_names(conn):
    if conn:
        try: 
            cursor = conn.cursor()
        
            # Retrieve portfolio names
            cursor.execute("SELECT id, name FROM Portfolio")
            portfolios = cursor.fetchall()
        
            return portfolios
        except sqlite3.Error as e:
            print(e)
    else:
        print("No database connection available.")
        return None

# Retrieve all stocks for the accordion.
def get_stock_names(conn):
    if conn:
        try: 
            cursor = conn.cursor()
        
            # Retrieve portfolio names
            cursor.execute("SELECT id, name, portfolio_id FROM Stock")
            stocks = cursor.fetchall()
        
            return stocks
        except sqlite3.Error as e:
            print(e)
    else:
        print("No database connection available.")
        return None
