import mysql.connector as SQLC

# Connect to the database
db = SQLC.connect(host="localhost", user="root", password="", database="Katzenjammer")
cursor = db.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS Katzenjammer")

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS ALBUMS (" \
    "AId INT PRIMARY KEY," \
    "Title VARCHAR(255) NOT NULL," \
    "Year INT NOT NULL," \
    "Label VARCHAR(255) NOT NULL)")

# Insert data by reading CSV
with open("ALBUMS.csv", "r") as file:
    next(file)  # Skip the header
    for line in file:
        a_id, title, year, label = line.strip().split(",")
        cursor.execute("INSERT INTO ALBUMS (AId, Title, Year, Label) VALUES (%i, %s, %i, %s)", 
                       (a_id, title, year, label))
    db.commit()