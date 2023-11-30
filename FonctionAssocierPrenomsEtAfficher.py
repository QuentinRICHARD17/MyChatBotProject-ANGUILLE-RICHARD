from FonctionExtraireNomsPresidents import *
from NotreLibrairie import *
def AfficherNomsPresidents():
    for i in range(len(files_names)):
        NomsPresidents.append(files_names[i][11:-4])
    print(NomsPresidents)




