'''

    Wordle Solver.

'''

from termcolor import colored
from os import system, path, mkdir

def main():

    if not path.exists('words/words.txt'):

        with open('words/words.txt', 'w') as file:
            pass

        # creates dictionary of only five letter words
        counter = 0
        with open('words/dictionary.txt', 'r') as file:
            for line in file:
                if (len(line.rstrip()) == 5):
                    with open('words/words.txt', 'a') as five:
                        five.write(line)
                        counter += 1

        print('There are {count} five letter words in the english language.'.format(count=counter))

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_stats = {}
    for char in alphabet:
        key_stats[char] = 0

    with open('words/words.txt', 'r') as file:
        for line in file:
            temp_line = line.rstrip()
            for char in temp_line:
                key_stats[char.lower()] += 1

    for char in alphabet:
        print('{character}: {count}'.format(character=char, count=key_stats[char]))


if __name__ == '__main__':
    system('cls')
    print(colored('ERROR: Please run from run.py', 'red'))