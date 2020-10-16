
def load_game() -> bool:
    from MemoryGame import play as memory_game_play
    from GuessGame import play as guess_game_play
    from CurrencyRouletteGame import play as currency_roulette_game_play
    from Score import add_score as add_score
    print(f"\t 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print(f"\t 2. Guess Game - guess a number and see if you chose like the computer")
    print(f"\t 3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    input_from_user_game_local = input(f"\n\t Please choose a game to play:")
    input_from_user_load_difficulty_local = input(f"\n\t Please choose game difficulty from 1 to 5:")

    if (0 < int(input_from_user_load_difficulty_local) <= 5) and (0 < int(input_from_user_game_local) <= 3):
        if int(input_from_user_game_local) == 1:
            if memory_game_play(int(input_from_user_load_difficulty_local)):
                add_score(int(input_from_user_load_difficulty_local))
                return True
            else:
                return False
        elif int(input_from_user_game_local) == 2:
            if guess_game_play(int(input_from_user_load_difficulty_local)):
                add_score(int(input_from_user_load_difficulty_local))
                return True
            else:
                return False
        elif int(input_from_user_game_local) == 3:
            if currency_roulette_game_play(int(input_from_user_load_difficulty_local)):
                add_score(int(input_from_user_load_difficulty_local))
                return True
            else:
                return False
    else:
        print(f"\n\t wrong option, choose a game from 1 to 3 and not " + " "
              + str(input_from_user_game_local) + "\n")
        print(f"\n\t wrong option, difficulty from 1 to 5 and not" + " "
              + str(input_from_user_load_difficulty_local) + "\n")
        return False


def welcome(name: str) -> None:
    print(f"Hello" + " " + name + " " + "and welcome to the World of Games (WoG).")
    print(f"Here you can find many cool games to play.\n")
    load_game()
    return
