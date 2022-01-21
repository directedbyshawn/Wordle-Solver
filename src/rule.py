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
        type = Type.Null
        char = ''
        position = -1
