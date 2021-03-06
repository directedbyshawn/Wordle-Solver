'''

    Setup.

'''

from os import path, mkdir
from src.config import WORDS_PATH, DICTIONARY_PATH, DB_PATH
from src.db import create_db, load_defaults

def main():

    # creates dictionary of only five letter words
    if not path.exists(WORDS_PATH):
        
        with open(WORDS_PATH, 'w') as file:
            pass
        
        # adds five letter words to separate dictionary
        with open(DICTIONARY_PATH, 'r') as file:
            for line in file:
                if (len(line.rstrip()) == 5):
                    with open(WORDS_PATH, 'a') as five:
                        five.write(line)

    # creates database directory
    if not path.exists('db'):
        mkdir('db')

    # creates dictionary to record letter frequencies
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_stats = {}
    for char in alphabet:
        key_stats[char] = 0

    # goes through each character in each word to record frequencies
    with open(WORDS_PATH, 'r') as file:
        for line in file:
            temp_line = line.rstrip()
            for char in temp_line:
                key_stats[char.lower()] += 1

    # creates database if it does not exist
    if not path.exists(DB_PATH):
        create_db()

    load_defaults(key_stats)

    # TODO: Call webscraper to get popularity ratings