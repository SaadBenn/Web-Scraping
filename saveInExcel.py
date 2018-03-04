# ********************************************
# ********************************************

def saveInExcel(fileName, database):

    if fileName.split('.')[-1] != 'xls' and fileName.split('.')[-1] != 'xlsx':
        print("Incorrect extension for the file!")
        return None

    import pandas as panda
    import sqlite3

    connection = sqlite3.connect(str(database))

    content = panda.read_sql_query("SELECT * FROM MovieInfo", connection)
    connection.close()

    content.to_excel(fileName, sheet_name='Movie Info')
