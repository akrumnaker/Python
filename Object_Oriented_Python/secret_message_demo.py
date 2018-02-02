# This script is a test of the secret_message.py script

import os

from Object_Oriented_Python import secret_message as sm

# the directory you want to check for the secret message
root_dir = "C:/Users/aaron/Desktop/prank"

file_names = os.listdir(root_dir)

sm.rename_files(file_names, root_dir)