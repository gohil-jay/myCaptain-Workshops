import sqlite3

def connect(dbname):
    con = sqlite3.connect(dbname)
    con.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT")

    print("Table created successfully!")

    con.close()
