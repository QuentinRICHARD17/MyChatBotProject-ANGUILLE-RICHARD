from FonctionTFAfficherOccurencesMots import *
from NotreLibrairie import *
from math import log
def CalculScoreIDF():
    for i in range(len(MaListeDeDico)):
        for cle in MaListeDeDico[i].keys():
            if cle in DictionnaireIDF:
                DictionnaireIDF[cle] += 1
            else:
                DictionnaireIDF[cle] = 1
    for mot , occurence in DictionnaireIDF.items():
        DictionnaireIDF[mot] = log(len(MaListeDeDico)/occurence)
    return DictionnaireIDF




