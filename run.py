'''

    Exec file for wordle solver.

'''

from main import main
import setup
from os import system, path
from src.config import DB_PATH

if __name__ == '__main__':
    system('cls')
    if not path.exists(DB_PATH):
        setup.setup()
    main()