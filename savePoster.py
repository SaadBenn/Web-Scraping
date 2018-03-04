
def savePoster(jsonFile):

    import os  # need to use the path, mkdir and open functions
    import urllib

    title = jsonFile['Title']
    posterURL = jsonFile['Poster']

    # Splits the poster url by '.' and picks up the last
    # string as file extension
    posterExtension = posterURL.split('.')[-1]
    # Reads the image file from web
    poster = urllib.request.urlopen(posterURL).read()

    saveLocation = os.getcwd() + '\\' + 'Posters' + '\\'

    if not os.path.isdir(saveLocation):
        os.mkdir(saveLocation)

    fileName = saveLocation + str(title) + '.' + posterExtension
    file = open(fileName, 'wb')

    file.write(poster)
    file.close()