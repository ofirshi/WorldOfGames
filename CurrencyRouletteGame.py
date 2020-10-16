
#   https://github.com/alexprengere/currencyconverter

from random import randint

random_number = int(randint(1, 100))


# c = CurrencyConverter()
# value = round(c.convert((random_number), 'USD', 'ILS'), 0)
# print(f"number of " + str(random_number) +"NIS" + " "+ "is " + str(value) +"USD")

# from datetime import date
# c.convert(100, 'EUR', 'USD', date=date(2013, 3, 21))


def get_money_interval(user_difficulty: int, random_number_local: int) -> str or tuple:
    from currency_converter import CurrencyConverter
    try:
        c = CurrencyConverter()
        # print(f"xxx" + str(random_number))
        value = round(c.convert(random_number_local, 'USD', 'ILS'))
        option1 = int(abs(int(value) - (5 - int(user_difficulty))))
        option2 = int(abs(int(value) + (5 - int(user_difficulty))))
        # print(option1,value,option2)
        return option1, option2
    except BaseException as e:
        print("unexpected error occurred:" + str(e))
        return False


def get_guess_from_user(random_number_local: int) -> int:
    input_guess_from_user = input(f"\nWhat is " + str(random_number_local) + "NIS" + " in USD ?\nenter a guess:")
    return int(input_guess_from_user)


def play(user_difficulty: int) -> bool:
    print(f"CurrencyRouletteGame" + " " + str(user_difficulty))
    get_random_nm = get_money_interval(user_difficulty, random_number)
    user_guess = get_guess_from_user(random_number)
    if (int(get_random_nm[0]) == int(user_guess) or int(user_guess) > int(get_random_nm[0])) and (
            int(get_random_nm[1]) == int(user_guess) or int(user_guess) < int(get_random_nm[1])):
        print("Won")
        return True
    else:
        print("Try again")
        return False
