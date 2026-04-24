import mysql.connector as SQLC

# Connect to the database
db = SQLC.connect(host="localhost", user="root", password="", database="Bakery")
cursor = db.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS Bakery")

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS RECEIPTS (" \
    "ReceiptNumber INT PRIMARY KEY," \
    "Date DATE NOT NULL," \
    "CustomerId INT NOT NULL FOREIGN KEY REFERENCES CUSTOMERS(Id),")

# Insert data by reading CSV
with open("RECEIPTS.csv", "r") as file:
    next(file)  # Skip the header
    for line in file:
        receipt_number, date, customer_id = line.strip().split(",")
        cursor.execute("INSERT INTO RECEIPTS (ReceiptNumber, Date, CustomerId) VALUES (%i, %s, %i)", 
                       (receipt_number, date, customer_id))
    db.commit()