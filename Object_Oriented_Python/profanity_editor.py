# This script contains functions designed to read a document and send
# the contents to a web url in order to check if there is any profanity
# in the document.

import time

import requests


def read_text(filename):
    """
    This function opens a file and reads the contents line by line.
    Each line is then checked for any profanity.
    :param filename: the file to read
    :return: None
    """
    with open(filename, 'r') as f:
        line = f.readline()
        line_num = 1
        while line != "":
            check_profanity(line, line_num)
            line = f.readline()
            line_num += 1


def check_profanity(text, line_num):
    """
    This function checks to see if the contents of text contain
    any profane words. It will send the text in a request to a
    website and obtain a response whether there are profane words
    in the text or not. The response is then formatted and printed
    to the user
    :param text: line of text to check
    :param line_num: the line number of the document that is being checked
    :return: None
    """
    response = requests.get("http://www.wdylike.appspot.com/?q="+text)
    if "true" in str(response.content):
        print("Profanity in line " + str(line_num))
    elif "false" in str(response.content):
        print("No profanity in line " + str(line_num))
    else:
        print("Could not read the line properly.")
    time.sleep(.25)
