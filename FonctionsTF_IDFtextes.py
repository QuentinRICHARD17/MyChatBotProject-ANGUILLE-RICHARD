from math import log
from NotreLibrairie import *

def CalculMatriceTF_IDF(DictionnaireIDF, ListeDicoTFtextes):
    matriceTF_IDF = []

    for cle in DictionnaireIDF.keys():
        ligne = []
        for i in range(len(ListeDicoTFtextes)):
            if cle in ListeDicoTFtextes[i]:
                ligne.append(ListeDicoTFtextes[i][cle] * DictionnaireIDF[cle])
            else:
                ligne.append(0.0)
        matriceTF_IDF.append(ligne)

    '''
    # Afficher la matrice
    for j in range(len(matriceTF_IDF)):
        for k in range(len(matriceTF_IDF[j])):
            print(matriceTF_IDF[j][k], end=' ')
        print()
    '''
    return matriceTF_IDF



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
    ListeDicoTFtextes.append(OccurencesMotsTexte)

    return ListeDicoTFtextes


def CalculScoreIDF(ListeDicoTFtextes):

    DictionnaireIDF = {}

    for i in range(len(ListeDicoTFtextes)):
        for cle in ListeDicoTFtextes[i].keys():
            if cle in DictionnaireIDF:
                DictionnaireIDF[cle] += 1
            else:
                DictionnaireIDF[cle] = 1

    total_textes = len(ListeDicoTFtextes)

    for mot, occurence in DictionnaireIDF.items():
        DictionnaireIDF[mot] = log(total_textes / occurence)

    return DictionnaireIDF




def TransposeeMatriceTF_IDF(matrice):

    nombre_lignes = len(matrice)
    nombre_colonnes = len(matrice[0])

    # Créer une matrice transposée avec des listes vides
    matriceTransposee = [[] for i in range(nombre_colonnes)]

    # Remplir la matrice transposée en échangeant les lignes et les colonnes
    for i in range(nombre_lignes):
        for j in range(nombre_colonnes):
            matriceTransposee[j].append(matrice[i][j])
    '''
    # Afficher la matrice
    for j in range(len(matriceTransposee)):
        for k in range(len(matriceTransposee[j])):
            print(matriceTransposee[j][k], end=' ')
        print()
    '''
    return matriceTransposee



