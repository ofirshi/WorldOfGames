# A general purpose python file. This file will contain general information and operations we need
# for our game.
# 1. SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
# 2. BAD_RETURN_CODE - A number representing a bad return code for a function.
# 3. Screen_cleaner - A function to clear the screen (useful when playing memory game or
# before a new game starts).

import time
import os
from typing import Any, Union

scores_file_name: str = "Scores.txt"
bad_return_code = "200"
script_path = os.path.dirname(os.path.abspath(__file__))
file_full_path: Union[str, Any] = script_path + '\\' + scores_file_name


def cls3():
    print("hello world", end='')
    time.sleep(0)
    print("\r               ")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def cls2():  # cls2 = lambda: print('\n\t' * 100)
    print('\n\t' * 100)


def screen_cleaner():
    cls()
    cls2()
    cls3()
