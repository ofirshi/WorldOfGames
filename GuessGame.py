

def generate_number(get_user_difficulty: int) -> int:
    import random
    # Will generate number between 1 to difficulty and save it to  secret_number.
    secret_number = random.randint(1, int(get_user_difficulty))
    return secret_number


def get_guess_from_user(user_difficulty: int, secret_number: str) -> bool or str:
    # Will prompt the user for a number between 1 to difficulty and return the number.
    # print(f"secret_number" + " " + str(secret_number)) # - > print secret_number
    try:
        user_input = input("\n\tPlease enter a number between 1 to" + " " + str(user_difficulty) + ":")
        if int(user_input) > int(user_difficulty):
            return "Error"
        else:
            results = compare_results(secret_number, user_input)
            return results
    except ValueError as err:
        print(err.args)


def compare_results(secret: str, get_number_from_user: str) -> bool:
    # Will compare the the secret generated number to the one prompted by the get_guess_from_user.
    if str(secret) == str(get_number_from_user):
        return True
    else:
        return False


def play(input_from_user: int) -> bool:
    try:
        # Will call the functions above and play the game. Will return True / False if the user lost or won.
        get_user_difficulty = int(input_from_user)
        secret_number = str(generate_number(get_user_difficulty))  # -> return (secret_number)
        number_from_user = (str(get_guess_from_user(get_user_difficulty, secret_number)))  # -> return user_input
        # print(f"number_from_user" + " " + str(number_from_user))
        if str(number_from_user) == "False":
            print(f"Try again , Secret number was:" + " " + str(secret_number))
            return False
        elif str(number_from_user) == "Error":
            print("Try again")
            return False
        else:
            print("Won")
            return True
    except BaseException as e:
        print(f"unexpected error occurred:" + str(e))
        return False
