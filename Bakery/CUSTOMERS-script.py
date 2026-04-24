import mysql.connector as SQLC

# Connect to the database
db = SQLC.connect(host="localhost", user="root", password="", database="Bakery")
cursor = db.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS Bakery")

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMERS (" \
    "Id INT PRIMARY KEY," \
    "LastName VARCHAR(50)," \
    "FirstName VARCHAR(50))")

# Insert data by reading CSV
with open("CUSTOMERS.csv", "r") as file:
    next(file)  # Skip the header
    for line in file:
        id, last_name, first_name = line.strip().split(",")
        cursor.execute("INSERT INTO CUSTOMERS (Id, LastName, FirstName) VALUES (%i, %s, %s)", 
                       (id, last_name, first_name))
    db.commit()