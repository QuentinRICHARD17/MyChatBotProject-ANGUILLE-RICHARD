import os
from NotreLibrairie import *
def list_of_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names



def AfficherNomsPresidents():
    for i in range(len(files_names)):
        if files_names[i][-5].isdigit():
            name = files_names[i][11:-5]
        else:
            name = files_names[i][11:-4]
        if name not in NomsPresidents:
            NomsPresidents.append(name)
    print(NomsPresidents)
