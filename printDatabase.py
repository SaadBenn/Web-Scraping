# ********************************************
def printDatabase(database):
    import sqlite3

    connection = sqlite3.connect(str(database))
    cur = connection.cursor()

    for row in cur.execute('SELECT * FROM MovieInfo'):
        print(row)

    connection.close()
