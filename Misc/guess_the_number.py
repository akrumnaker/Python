import random


def get_number():
    """
    Grabs a random number between 1 and 100
    :return: number between 1 and 100 (integer)
    """
    return random.randrange(1, 101)


def prompt_guess():
    """
    Prompt the user to guess the secret number
    :return: guess (integer)
    """
    guess = input("Guess a number between 1 and 100:\t")
    while not validate_guess(guess):
        guess = input("Please give a number between 1 and 100:\t")
    return int(guess)


def validate_guess(guess):
    """
    Validates the guess provided by the user to determine if it
    is a numeric value
    :param guess: the guess provided by the user (str)
    :return: True or False
    """
    return str(guess).isnumeric()


def check_guess(guess, actual):
    """
    Check to see if the guess is lower, greater, or equal to
    the actual secret number
    :param guess: the user's number (integer)
    :param actual: the secret number (integer)
    :return: True or False
    """
    if guess < actual:
        print("Too low")
        return False
    elif guess > actual:
        print("Too high")
        return False
    else:
        print("That's the number!")
        return True
