# A package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number. That number is the accumulation of the
# winnings of the user. Amount of points for winning a game is as follows:
# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he one will be added to his current amount of
# point saved in a file.
# Methods
# 1. add_score - The function’s input is a variable called difficulty. The function will try to read
# the current score in the scores file, if it fails it will create a new one and will use it to save
# the current score.


def add_score(difficulty: int) -> None:
    """

    :param difficulty:
    :return:
    """
    file_name: str = "Scores.txt"

    """

    :rtype: object
    """
    math = int
    if difficulty == 0:
        f = open(file_name, "w+")
        f.close()
    else:
        points_of_winning = (difficulty * 3) + 5
        try:
            f = open(file_name, "x")
            f.write(str(points_of_winning))
            f.close()
        except FileExistsError:
            f = open(file_name, "r")
            try:
                contents = f.read()
                math = int(str(contents)) + int(points_of_winning)
            except Exception:
                math = int(points_of_winning)
            finally:
                f = open(file_name, "w")
                f.write(str(math))
                print(str(math))
                f.close()
    return
    # print (difficulty , file_name)
