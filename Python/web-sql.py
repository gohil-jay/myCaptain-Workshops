import sqlite3

def connect(dbname):
    con = sqlite3.connect(dbname)
    con.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT")

    print("Table created successfully!")

    con.close()

def insert(dbname, values):
    con = sqlite3.connect(dbname)
    print("Inserted into the table: " + str(values))
    insert = "INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES (?, ?, ?, ?, ?)"
    con.execute(insert, values)
    con.commit()
    con.close()

    
def get_hotel_info(dbname):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("SELECT * FROM OYO_HOTELS")

    table_data = cur.fetchall()

    for record in table_data:
        print(record)

    con.close()
