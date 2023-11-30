import os
from NotreLibrairie import *
def list_of_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
