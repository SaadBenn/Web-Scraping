import json
from SearchMovie import searchMovie
from printDatabase import printDatabase
from extractKey import extractKey

# ********************************************

if __name__ == '__main__':

    title = input('\nEnter the name of a movie (enter \'quit\' or hit ENTER to quit): ')
    fileName = ''

    dict = extractKey()

    serviceurl, apikey = dict['serviceurl'], dict['apikey']

    while (title is not 'quit') and title != '':
        fileName = searchMovie(title, serviceurl, apikey)
        title = input('\nEnter the name of a movie (enter \'quit\' or hit ENTER to quit): ')

    print("Before you go, here is your stored information!")
    print('-' * 50)
    printDatabase(fileName)
    print('-' * 50)
    print("Catch you on the flip side!")
