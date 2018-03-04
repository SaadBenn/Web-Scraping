# ********************************************
def printJson(jsonFile):
    list_keys = ['Title', 'Year', 'Rated', 'Released', 'Runtime',
                 'Genre', 'Director', 'Writer', 'Actors', 'Plot',
                 'Language', 'Country', 'Awards', 'Ratings',
                 'Metascore', 'imdbRating', 'imdbVotes', 'imdbID']

    print('-' * 50)
    for element in list_keys:
        if element in list(jsonFile.keys()):
            print(f"{element}: {jsonFile[element]}")
    print('-' * 50)