import random


def roll_die(low, hi):
    """
    Simulate the rolling of a die by selecting a random number between
    low and hi inclusively.
    :param low: loq number on the die (integer )
    :param hi: high number on the die (integer)
    :return:
    """
    return random.randrange(low, hi + 1)


def prompt_continue():
    """
    Prompts the user whether they want to continue or not.
    Handles invalid responses until a valid one is provided.
    :return: "y" or "n"
    """
    res = input("Roll again? y / n:\t")
    res = res.lower()
    while (res != "y") and (res != "n"):
        print("Can't understand " + res)
        res = input("Roll again? y / n:\t")
        res = res.lower()
    return res


def prompt_dice():
    """
    Prompts the user for the low and high values of the die.
    Handles cases where low is greater than or equal to high.
    :return: low and high as a tuple
    """
    num1 = int(input("Low number on dice:\t"))
    num2 = int(input("High number on dice:\t"))
    while num1 >= num2:
        print("Low cannot be greater than or equal to high")
        num1 = int(input("Low number on dice:\t"))
        num2 = int(input("High number on dice:\t"))
    return num1, num2
