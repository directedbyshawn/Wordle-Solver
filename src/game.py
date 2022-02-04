'''

    Game class for wordle solver.

'''

from .rule import Rule, Type
from .word import Word
from .db import retrieve_words

class Game():

    def __init__(self):
        self.possible_words: Word = []
        self.correct_word: str = ''
        self.duplicates: list = []
        self.rules: Rule = []
        self.__load_words()

    def __load_words (self):

        ''' Loads words from database'''
        words = retrieve_words()

        for word in words:
            this_word = Word(word[0], word[1], word[2], word[3])
            self.possible_words.append(this_word)

    def print_words(self):
        for word in self.possible_words:
            print(word)

    def add_rule(self):
        pass

    def __update_words(self):
        pass