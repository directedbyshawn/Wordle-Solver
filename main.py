'''

    Wordle Solver.

'''

from termcolor import colored
from os import system, path, mkdir
from nerodia.browser import Browser

def main():

    # calls setup to create dictionaries and get letter frequency stats
    setup()

def setup():

    # creates dictionary of only five letter words
    if not path.exists('words/words.txt'):
        
        with open('words/words.txt', 'w') as file:
            pass
        
        # adds five letter words to separate dictionary
        with open('words/dictionary.txt', 'r') as file:
            for line in file:
                if (len(line.rstrip()) == 5):
                    with open('words/words.txt', 'a') as five:
                        five.write(line)

    # creates dictionary to record letter frequencies
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_stats = {}
    for char in alphabet:
        key_stats[char] = 0

    # goes through each character in each word to record frequencies
    with open('words/words.txt', 'r') as file:
        for line in file:
            temp_line = line.rstrip()
            for char in temp_line:
                key_stats[char.lower()] += 1

    for char in alphabet:
        #print('{character}: {count}'.format(character=char, count=key_stats[char]))
        pass

if __name__ == '__main__':
    system('cls')
    print(colored('ERROR: Please run from run.py', 'red'))