import mysql.connector as SQLC

# Connect to the database
db = SQLC.connect(host="localhost", user="root", password="", database="Bakery")
cursor = db.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS Bakery")

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS ITEMS (" \
    "Receipt INT NOT NULL FOREIGN KEY REFERENCES RECEIPTS(ReceiptNumber)," \
    "Ordinal INT NOT NULL," \
    "Item INT NOT NULL FOREIGN KEY REFERENCES GOODS(Id)," \
    "PRIMARY KEY (Receipt, Ordinal),")

# Insert data by reading CSV
with open("ITEMS.csv", "r") as file:
    next(file)  # Skip the header
    for line in file:
        receipt, ordinal, item = line.strip().split(",")
        cursor.execute("INSERT INTO ITEMS (Receipt, Ordinal, Item) VALUES (%i, %i, %i)", 
                       (receipt, ordinal, item))
    db.commit()