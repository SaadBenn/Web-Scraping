def saveInDatabase(json_file):

	import sqlite3   #get the library
	
	# get file name from the user as input
	fileName = input(
		"""Please enter the name for the file.
		""")
	fileName = fileName + '.sqlite3' #extension added


	connection = sqlite3.connect(str(fileName)) #establish a connection
	cur = connection.cursor() 

	title = json_file['Title']

	if (json_file['Year'] != 'N/A'):
		year = int(json_file['Year']) #cast it to integer so we can manipulate
	if (json_file['Runtime'] != 'N/A'):
		runTime = int(json_file['Runtime'].split()[0]) #get the timing only
	if (json_file['Metascore'] != 'N/A'): 
		metaScore = float(json_file['Metascore'])
	else: 
		metaScore = -1

	if (json_file['imdbRating'] != 'N/A' ):
		imdbRating = float(json_file['imdbRating'])
	else: 
		imdbRating = -1 

	if (json_file['Genre'] != 'N/A'):
		genre = json_file['Genre']

		
# create the database

	cur.execute(""" 
		CREATE TABLE IF NOT EXISTS MOVIEINFO
		Title TEXT,
		Year INTEGER,
		Runtime INTEGER,
		MetaScore REAL,
		IMDBRating REAL,
		Genre TEXT 
		""")

	cur.execute('SELECT Title FROM MovieInfo WHERE Title = ?', (title,))
	row = cur.fetchone()

	if row is None:
		cur.execute("""
			INSERT INTO MovieInfo
			(Title, Year, Runtime, MetaScore, IMDBRating, Genre)
			VALUES (?,?,?,?,?,?)""",
			(title,year, runTime, metaScore, imdbRating, genre))
	else: 
		print("Database contains the query.")

	# flush the data into the database
	connection.commit()
	#close the connection
	connection.close()					
