'''

    Word class for wordle solver.

'''

class Word():

    def __init__(self):
        self.id = -1
        self.word = ''
        self.frequency_rating = 0
        self.popularity_rating = 0

    def __init__(self, id: int, word: str, frequency: int, popularity: int):
        self.id = id
        self.word = word
        self.frequency_rating = frequency
        self.popularity_rating = popularity

    def __repr__(self):
        return '{id}: {word}, freq={frequency} & pop={popularity}\n'.format(id=self.id, word=self.word, frequency=self.frequency_rating, popularity=self.popularity_rating)

    def increment_popularity(self):
        self.popularity_rating += 1

        