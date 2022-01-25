'''

    Database configuration for wordle solver

'''

import sqlite3
from .config import DB_PATH, WORDS_PATH
from os.path import exists

def create_db():

    conn = ''
    cursor = ''

    if not exists(DB_PATH):

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE words (
            word text,
            frequency int,
            popularity int
        )''')
        conn.commit()

        conn = None
        cursor = None

def load_defaults(stats):

    with open(WORDS_PATH, 'r') as words_file:
        for word in words_file:
            print(word.rstrip())


def add_word(word, frequency, popularity):
    pass


    
