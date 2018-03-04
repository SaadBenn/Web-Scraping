import json
# open the json file and extract the omdb API key

def extractKey():

    dict = {}
    with open('APIkeys.json') as file:
        keys = json.load(file)
        omdbApi = keys['OMDBapi']

    dict['serviceurl'] = 'http://www.omdbapi.com/?'
    dict['apikey'] = '&apikey=' + omdbApi

    return dict
