'''

    Database configuration for wordle solver

'''

import sqlite3
from .config import DB_PATH, WORDS_PATH
from os.path import exists
from time import sleep
from os import system
from termcolor import colored

def create_db():

    conn = ''
    cursor = ''

    if not exists(DB_PATH):

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE words (
            id int,
            word text,
            frequency int,
            popularity int
        )''')

        conn.commit()

        conn = None
        cursor = None

def load_defaults(stats):

    ''' Calculates frequency ranking of each word and adds the word '''

    with open(WORDS_PATH, 'r') as words_file:
        id = 1
        for word in words_file:
            current_word = word.rstrip()
            current_frequency = 0
            for char in current_word:
                current_frequency += stats[char]
            add_word(id, current_word, current_frequency, 0)
            id += 1

def has_no_repetition(word):

    letters = []

    for char in word:
        if char in letters:
            return False
        else:
            letters.append(char)

    return True


def add_word(id, word, frequency, popularity):
    
    ''' Adds new word to the database '''

    data = [(id, word, frequency, popularity)]

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.executemany('INSERT INTO words VALUES (?, ?, ?, ?)', data)
        conn.commit()
    except sqlite3.IntegrityError:
        print(colored('ERROR: Attempt to add duplicate record.', 'red'))
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

def retrieve_words():

    words = []

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        for row in cursor.execute('SELECT * from words'):
            words.append(row)
    except sqlite3.DatabaseError:
        print('ERROR: Could not retrieve data')
    finally:
        try:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
        except Exception:
            print(colored('ERROR: Cant close connection to databse.', 'red'))

    return words
    
