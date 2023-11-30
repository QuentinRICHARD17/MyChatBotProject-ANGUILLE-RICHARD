from FonctionTFAfficherOccurencesMots import *
from FonctionIDF import *
from NotreLibrairie import *
def CalculMatriceTF_IDF():
    MatriceTF_IDF.append([' '] + [i + 1 for i in range(len(MaListeDeDico))])

    for cle in DictionnaireIDF.keys():
        L = [cle]
        for i in range(len(MaListeDeDico)):
            if cle in MaListeDeDico[i]:
                L.append(MaListeDeDico[i][cle] * DictionnaireIDF[cle])
            else:
                L.append(0.0)
        MatriceTF_IDF.append(L)

    for j in range(len(MatriceTF_IDF)):
        for k in range(len(MatriceTF_IDF[j])):
            print(MatriceTF_IDF[j][k], end=' ')
        print()
