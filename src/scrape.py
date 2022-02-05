'''

    Web scraper to get word probability.

'''

from selenium import webdriver
from .db import retrieve_words, update_results
from .game import Game
from time import sleep
from os import system

def scrape():

    # browser
    driver = webdriver.Chrome()

    # get list of all words from db
    words = retrieve_words()

    game = Game()

    for word in game.possible_words:
        try:
            if (word.popularity_rating == 0):
                url = get_url(word.word)
                driver.get(url)
                sleep(1.3)
                result_string = driver.find_element_by_id('result-stats').text
                result_split = result_string.split()
                word.popularity_rating = convert_num(result_split[1])
                update_results(word.id, word.popularity_rating)
                print('Word: {word}'.format(word=word))
        except Exception:
            score = input('Enter score manually or press enter to continue: ')
            if (score != '' and score != ' ' and score != '\n'):
                try:
                    word.popularity_rating = int(score)
                    update_results(word.id, word.popularity_rating)
                    print('Word: {word}'.format(word=word))
                except Exception:
                    print('Error with manual entry')

    system('cls')
    print('Finished search for all words.')

    

def get_url(search_term):

    url = 'https://www.google.com/search?q='

    if ' ' in search_term:
        terms = search_term.split()
        for term in terms:
            url += '{term}+'.format(term=term)
        url = url[0:len(url)-1]
    else:
        url += search_term

    return url

def convert_num(num_string):

    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']

    for char in num_string:
        if char not in chars:
            return -1

    if ',' in num_string:
        num_string = num_string.replace(',', '')

    num = int(num_string)

    return num


if __name__ == '__main__':
    scrape()