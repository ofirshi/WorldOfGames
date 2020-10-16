import time
import random
import os


input_from_user_load_difficulty: int = 0


def cls3():
    print("hello world", end='')
    time.sleep(0)
    print("\r               ")


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def cls2():  # cls2 = lambda: print('\n\t' * 100)
    print('\n\t' * 100)


def generate_sequence(user_load_difficulty: int) -> list:
    list_local = []
    a = 0
    while a < int(user_load_difficulty):
        # a = a + 1
        difficulty = random.randint(1, 101)
        list_local.append(str(difficulty))
        a = a + 1
    # print (list)
    return list_local


def get_list_from_user(user_load_difficulty: int) -> list:
    user_list = []
    a = 0
    while a < int(user_load_difficulty):
        user_input = input("Please add number:")
        user_list.append(str(user_input))
        a = a + 1
    return user_list


def is_list_equal(list_local: list, user_list: list) -> bool:
    if all(i in list_local for i in user_list):
        return True
        # return True
    else:
        return False
        # return False


def play(input_from_user_load_difficulty_local: int) -> bool:
    from Utils import screen_cleaner as screen_cleaner
    # print(f"MemoryGame" + " " + str(input_from_user_load_difficulty))
    list_gen = generate_sequence(input_from_user_load_difficulty_local)
    print(list_gen)
    time.sleep(0.7)
    screen_cleaner()
    user_list = get_list_from_user(input_from_user_load_difficulty_local)
    # print(user_list)
    list_equal = is_list_equal(list_gen, user_list)
    if list_equal:
        print("Won")
        return True
    else:
        print("try again")
        return False
