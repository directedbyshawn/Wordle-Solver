'''

    Word class for wordle solver.

'''

class Word():

    def __init__(self):
        self.word = ''
        self.frequency_rating = 0
        self.popularity_rating = 0

    def __init__(self, word: str, frequency: int, popularity: int):
        self.word = word
        self.frequency_rating = frequency
        self.popularity_rating = popularity

        