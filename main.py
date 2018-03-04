import urllib
import json
from saveInDatabase import saveInDatabase
#********************************************

#open the json file and extract the omdb API key
with open('APIkeys.json') as file:
	keys = json.load(file)
	omdbApi = keys['OMDBapi']

serviceurl = 'http://www.omdbapi.com/?'
apikey = '&apikey='+omdbApi


#********************************************
def printJson(jsonFile):
	list_keys = ['Title', 'Year', 'Rated', 'Released', 'Runtime', 
				'Genre', 'Director', 'Writer', 'Actors', 'Plot', 
				'Language', 'Country', 'Awards', 'Ratings', 
               'Metascore', 'imdbRating', 'imdbVotes', 'imdbID']

               
    print('-'*50)
    for element in list_keys:
    	if element in list(jsonFile.keys()):
    		print("{element}: {jsonFile[element]}")
    print('-'*50)


#********************************************    
def savePoster(jsonFile):
	import os #need to use the path, mkdir and open functions

	title = jsonFile['Title']
	posterURL = jsonFile['Poster']

	# Splits the poster url by '.' and picks up the last 
	# string as file extension
	posterExtension = posterURL.split('.')[-1]
	# Reads the image file from web
	poster = urllib.request.urlopen(posterURL.read())

	saveLocation = os.getcwd() + '\\' + 'Posters' + '\\'

	if not os.path.isdir(saveLocation):
		os.mkdir(saveLocation)


	fileName = saveLocation + str(title) + '.' + posterExtension
	file = open( fileName, 'wb')

	file.write(poster)
	file.close()	

#******************************************** 

# call the function by passing in the json file
saveInDatabase(jsonFile)


#******************************************** 
def printDatabase(database):

	import sqlite3

	connection = sqlite3.connect(str(database))
	cur = connection.cursor()

	for row in cur.execute('SELECT * FROM MovieInfo'):
		print row

	connection.close()	


#******************************************** 
def saveInExcel(fileName, database):
	
	if	fileName.split('.')[-1]!= 'xls' and fileName.split('.')[-1] != 'xlsx':
		print("Incorrect extension for the file!")
		return None

	import pandas as panda
	import sqlite3

	connection = sqlite3.connect(str(database))

	content = panda.read_sql_query("SELECT * FROM MovieInfosql, connection")
	connection.close()

	content.to_excel(fileName, sheet_name='Movie Info')


#******************************************** 
def searchMovie(title):
	if(title.length() < 1 or title == 'quit'):
		print("Catch you on the flip side!")
		return None

	try:
		URL = serviceurl + urllib.parse.urlencode({'t': title})+apikey
        print('Retrieving the data of "{title}" now... ')
        
        uh = urllib.request.urlopen(URL)
        data = uh.read()
        jsonFile = json.loads(data)

        if jsonFile['Response'] =='True':
            printJson(jsonFile)
            
            # Asks user whether to download the poster of the movie
            if jsonFile['Poster'] != 'N/A':
                isDownloadPoster = input ('Poster of this movie can be downloaded. Enter "yes" or "no": ').lower()
                
                if isDownloadPoster == 'yes':
                    savePoster(jsonFile)

            # Asks user whether to save the movie information in a local database
            isDatabaseLocal = input ('Save the movie info in a local database? Enter "yes" or "no": ').lower()
            if isDatabaseLocal == 'yes':
                saveInDatabase(jsonFile)
        
        else:
            print("Error encountered: ", jsonFile['Error'])
	
	except urllib.error.URLError as e:
		print('ERROR: {e.reason()}')
		

if __name__ == '__main__':

	title = input('\nEnter the name of a movie (enter \'quit\' or hit ENTER to quit): ')

	while ((title is not 'quit') or (title)):
		searchMovie(title)

	print("Before you go, here is your stored information!")
	print('-'*50)	
	printDatabase('movies.sqlite3')
	print('-'*50)	
	print("Catch you on the flip side!")	

