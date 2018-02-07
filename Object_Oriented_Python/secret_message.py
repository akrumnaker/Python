# This script is used to find a secret message hidden within
# using the names of files. (This script if fairly specific,
# and would not function as intended with random files).

import os


def cleanup_file_name(file):
    """
    This function will loop through all the characters of
    a filename and will return a string containing only
    characters that are not digits
    :param file: the file name that needs to cleaned up
    :return: file name without any numbers in it
    """
    clean_name = ""
    # loop through the characters in the filename
    for index in range(len(file)):
        # add character to clean_name if the character is not a digit
        if not str.isdigit(file[index]):
            clean_name += file[index]

    return clean_name


def rename_files(files, path):
    """
    This function will rename all the file names in files in
    the directory at the end of path
    :param files: list of files found at the end of path
    :param path: the path to the files
    :return:
    """
    for file in files:
        clean_name = cleanup_file_name(file)
        print("old name: " + file)
        print("new name: " + clean_name)
        os.rename(path + "/" + file, path + "/" + clean_name)
