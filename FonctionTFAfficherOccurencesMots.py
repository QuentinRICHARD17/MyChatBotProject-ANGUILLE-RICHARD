from NotreLibrairie import *
def CalculScoreTF(CleanedDirectory):
    with open(CleanedDirectory, 'r', encoding='utf-8') as ReadTexte:
        contenu = ReadTexte.read()
    OccurencesMotsTexte = {}
    i = 0
    j = 0
    while i < len(contenu):
        while i < len(contenu) and ord(contenu[i]) == 32:
            i += 1
        j = i
        while j < len(contenu) and ord(contenu[j]) != 32:
            j += 1
        if i < j:
            mot = contenu[i:j]
            if mot in OccurencesMotsTexte:
                OccurencesMotsTexte[mot] += 1
            else:
                OccurencesMotsTexte[mot] = 1
        i = j + 1
    MaListeDeDico.append(OccurencesMotsTexte)
    return OccurencesMotsTexte
