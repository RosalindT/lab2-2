import mysql.connector as SQLC

# Connect to the database
db = SQLC.connect(host="localhost", user="root", password="", database="Katzenjammer")
cursor = db.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS Katzenjammer")

# Create the table
cursor.execute("CREATE TABLE IF NOT EXISTS TRACKLISTS (" \
    "AlbumId INT NOT NULL," \
    "Position INT NOT NULL," \
    "SongId INT NOT NULL UNIQUE," \
    "PRIMARY KEY (AlbumId, Position)," \
    "FOREIGN KEY (AlbumId) REFERENCES ALBUMS(AId)," \
    "FOREIGN KEY (SongId) REFERENCES SONGS(SongId))")

# Insert data by reading CSV
with open("TRACKLISTS.csv", "r") as file:
    next(file)  # Skip the header
    for line in file:
        album_id, position, song_id = line.strip().split(",")
        cursor.execute("INSERT INTO TRACKLISTS (AlbumId, Position, SongId) VALUES (%i, %i, %i)", 
                       (album_id, position, song_id))
    db.commit()