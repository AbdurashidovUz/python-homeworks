import sqlite3

with sqlite3.connect('library.db') as con:
    cursor=con.cursor()
    cursor.execute("DROP TABLE IF EXISTS Books")
    cursor.execute("CREATE TABLE Books(Title TEXT, Author TEXT, Year_Published INT, Genre TEXT)")
    data=[
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ]

    placeholders = ", ".join(['?'] * 4)
    cursor.executemany(f"INSERT INTO Books VALUES({placeholders})", data)

    cursor.execute("UPDATE Books SET Year_Published=1950 WHERE Title == '1984'")

    cursor.execute("Select Title, Author from Books Where Genre = 'Dystopian'")
    print(cursor.fetchall())

    cursor.execute("Delete from Books where Year_Published < 1950")

    cursor.execute("ALTER TABLE Books ADD column Rating INT")

    cursor.execute("UPDATE Books SET Rating=4.8 WHERE Title == 'To Kill a Mockingbird'")
    cursor.execute("UPDATE Books SET Rating=4.7 WHERE Title == '1984'")
    cursor.execute("UPDATE Books SET Rating=4.5 WHERE Title == 'The Great Gatsby'")

    cursor.execute("Select * From Books order by Year_Published asc ")
    print(cursor.fetchall())