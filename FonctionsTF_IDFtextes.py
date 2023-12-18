from math import log
from NotreLibrairie import *

def CalculMatriceTF_IDF(DictionnaireIDF, ListeDicoTFtextes):

    MatriceTF_IDF = []

    MatriceTF_IDF.append([' '] + [i + 1 for i in range(len(ListeDicoTFtextes))])

    for cle in DictionnaireIDF.keys():
        L = [cle]
        for i in range(len(ListeDicoTFtextes)):
            if cle in ListeDicoTFtextes[i]:
                L.append(ListeDicoTFtextes[i][cle] * DictionnaireIDF[cle])
            else:
                L.append(0.0)
        MatriceTF_IDF.append(L)
    
    # Afficher la matrice
    rep = input("Voulez vous voir la matrice ? (répondre par 'oui' ou 'non') :")
    if rep == "oui":
        for j in range(len(MatriceTF_IDF)):
            for k in range(len(MatriceTF_IDF[j])):
                print(MatriceTF_IDF[j][k], end=' ')
            print()
    
    return MatriceTF_IDF



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
    for mot , occurence in DictionnaireIDF.items():
        DictionnaireIDF[mot] = log(len(ListeDicoTFtextes)/occurence)
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

    # Afficher la matrice
    rep = input("Voulez vous voir la matrice transposée ? (répondre par 'oui' ou 'non') :")
    if rep == "oui":
        for j in range(len(matriceTransposee)):
            for k in range(len(matriceTransposee[j])):
                print(matriceTransposee[j][k], end=' ')
            print()

    return matriceTransposee
