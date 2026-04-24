import mysql.connector as SQLC

# Connect to the database
db = SQLC.connect(host="localhost", user="root", password="", database="Katzenjammer")
cursor = db.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS Katzenjammer")

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS SONGS (" \
    "SongId INT PRIMARY KEY," \
    "Title VARCHAR(255) NOT NULL)")

# Insert data by reading CSV
with open("SONGS.csv", "r") as file:
    next(file)  # Skip the header
    for line in file:
        song_id, title = line.strip().split(",")
        cursor.execute("INSERT INTO SONGS (SongId, Title) VALUES (%i, %s)", 
                       (song_id, title))
    db.commit()