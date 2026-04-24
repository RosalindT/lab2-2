import mysql.connector as SQLC

# Connect to the database
db = SQLC.connect(host="localhost", user="root", password="", database="Katzenjammer")
cursor = db.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS Katzenjammer")

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS BAND (" \
    "Id INT PRIMARY KEY," \
    "FirstName VARCHAR(30) NOT NULL," \
    "LastName VARCHAR(30) NOT NULL)")

# Insert data by reading CSV
with open("BAND.csv", "r") as file:
    next(file)  # Skip the header
    for line in file:
        b_id, first_name, last_name = line.strip().split(",")
        cursor.execute("INSERT INTO BAND (Id, FirstName, LastName) VALUES (%i, %s, %s)", 
                       (b_id, first_name, last_name))
    db.commit()