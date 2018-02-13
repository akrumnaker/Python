import random

# may add more
ad_libs = ["First, you need to take the {x[0]} and then {x[1]} it all over the {x[2]} {x[3]}. " +
           "Next, take the {x[4]} butter and spread it {x[5]}. Now, put them together and enjoy your {x[6]}."]


def select_ad_lib():
    """
    Obtains an index to one of the ad libs in the ad_libs list
    :return: a valid index of the ad_libs list
    """
    return random.randrange(0, len(ad_libs))


def prompt_words(index):
    """
    Prompts the user for words to insert into the ad lib
    :param index: index of the selected ad lib
    :return: list containing words provided by user
    """
    words = []
    if index == 0:
        for i in range(7):
            if i == 0 or i == 3 or i == 4 or i == 6:
                words.append(input("Please give a noun:\t"))
            elif i == 1:
                words.append(input("Please give a verb:\t"))
            elif i == 2:
                words.append(input("Please give an adjective:\t"))
            else:
                words.append(input("Please give an adverb:\t"))

    return words


def build_ad_lib(words, index):
    """
    Inserts the words provided by the user into the ad lib
    :param words: list of words provided by the user
    :param index: index of the ad lib
    :return: ad lib with the list of words inserted
    """
    return ad_libs[index].format(x=words)
