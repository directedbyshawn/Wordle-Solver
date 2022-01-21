'''

    Rule class for wordle solver.

'''

import enum

class Type(enum.Enum):
    Null = 0
    Not = 1
    Contains = 2
    Position = 3


class Rule():

    def __init__(self):
        ruleType = Type.Null
        char = ''
        position = -1

    def check_word(self, word) -> bool:
        return True
