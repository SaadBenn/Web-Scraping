import urllib
import json
from saveInDatabase import saveInDatabase
from savePoster import savePoster
from printJSON import printJson
from saveInExcel import saveInExcel

# ********************************************
def searchMovie(title, serviceurl, apikey):
    if len(title) < 1 or title == 'quit':
        print("Catch you on the flip side!")
        return None

    try:
        URL = serviceurl + urllib.parse.urlencode({'t': title}) + apikey
        print(f'Retrieving the data of "{title}" now... ')

        uh = urllib.request.urlopen(URL)
        data = uh.read()
        jsonFile = json.loads(data)

        if jsonFile['Response'] == 'True':
            printJson(jsonFile)

            # Asks user whether to download the poster of the movie
            if jsonFile['Poster'] != 'N/A':
                isDownloadPoster = input('Poster of this movie can be downloaded. Enter "yes" or "no": ').lower()

                if isDownloadPoster == 'yes':
                    savePoster(jsonFile)

            # Asks user whether to save the movie information in a local database
            isDatabaseLocal = input('Save the movie info in a local database? Enter "yes" or "no": ').lower()

            if isDatabaseLocal == 'yes':
                fileName = saveInDatabase(jsonFile)
                saveAsExcel = input('Save the movie info in an excel file? Enter "yes" or "no": ').lower()

                if saveAsExcel == 'yes':
                    excelFileName = input('''Please enter the name for the excel file. No extension required!''')
                    excelFileName += '.xls'
                    saveInExcel(excelFileName, fileName)

                return fileName

        else:
            print("Error encountered: ", jsonFile['Error'])

    except urllib.error.URLError as e:
        print('ERROR: {e.reason()}')