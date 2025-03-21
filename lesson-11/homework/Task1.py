import sqlite3

with sqlite3.connect("roster.db") as connection:
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS Roster")
    cursor.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, Age INT)")

    data = [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]

    cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?)", data)

    cursor.execute("UPDATE Roster SET Name='Ezri Dax' WHERE Name == 'Jadzia Dax'")

    cursor.execute("Select Name,Age From Roster Where Species == 'Bajoran'")
    print(cursor.fetchall())

    cursor.execute("Delete from Roster where Age>100")

    cursor.execute("ALTER TABLE Roster ADD column Rank TEXT")

    cursor.execute("UPDATE Roster SET Rank='Captain' WHERE Name == 'Benjamin Sisko'")
    cursor.execute("UPDATE Roster SET Rank='Lieutenant' WHERE Name == 'Ezri Dax'")
    cursor.execute("UPDATE Roster SET Rank='Major' WHERE Name == 'Kira Nerys'")

    cursor.execute("Select * From Roster order by Age desc ")
    print(cursor.fetchall())

