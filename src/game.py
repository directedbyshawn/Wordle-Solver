'''

    Game class for wordle solver.

'''

from .rule import Rule, Type
from .word import Word

class Game():

    def __init__(self):
        self.possible_words: Word = []
        self.rules: Rule = []
        self.__load_words()

    def __load_words (self):
        ''' Loads words from database'''
        pass

    def add_rule(self):
        pass

    def __update_words(self):
        pass