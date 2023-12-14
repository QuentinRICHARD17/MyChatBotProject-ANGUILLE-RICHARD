from FonctionsTraitementTextes import *
from FonctionsExtractionNomsPresidents import *
#1
def AfficherMotsLesMoinsImportants(MatriceTF_IDF):
    for i in range(1, len(MatriceTF_IDF)):
        compteur = 0
        for j in range(1, len(MatriceTF_IDF[i])):
            if MatriceTF_IDF[i][j] != 0.0:
                compteur += 1
        if compteur == 0:
            ListMotsPasImportant.append(MatriceTF_IDF[i][0])
    print("Les mots les moins importants du dossier sont:", end=' ')
    for k in range(len(ListMotsPasImportant) - 1):
        print(ListMotsPasImportant[k], ",", end=' ')
    print(ListMotsPasImportant[k + 1])

#2

def AfficherMotsAvecScoreTF_IDFLePlusHaut(MatriceTF_IDF):
    ScoreLePlusHaut = 0
    for i in range(1 , len(MatriceTF_IDF)):
        for j in range(1, len(MatriceTF_IDF[i])):
            if MatriceTF_IDF[i][j] >= ScoreLePlusHaut:
                ScoreLePlusHaut = MatriceTF_IDF[i][j]
    print("Le(s) mot(s) ayant le score TF-IDF le plus élevé est(sont):", end=' ')
    for k in range(1 , len(MatriceTF_IDF)):
        for l in range(1 , len(MatriceTF_IDF[k])):
            if MatriceTF_IDF[k][l] == ScoreLePlusHaut:
                print(MatriceTF_IDF[k][0], ' ', end=' ')
    print()

#3

def AfficheMotLePlusRepeteParUnPresident(nom):
    L = []
    for i in range(len(files_names)):
        if nom in files_names[i]:
            L.append(i)

    print("Le(s) mot(s) le(s) plus répété(s) par", nom, "est(sont):")
    for j in range(len(L)):
        KeyMaxVal = max(ListeDicoTFtextes[L[j]] , key = ListeDicoTFtextes[L[j]].get)
        for cle , valeur in ListeDicoTFtextes[L[j]].items():
            if valeur == ListeDicoTFtextes[L[j]][KeyMaxVal]:
                print("Dans le texte", j, ':', cle)

#4
def ExtraireMotFrequent(liste_textes, liste_dictionnaire):
    mot_recherche = "nation"
    nb_max = 0
    texte_max = None

    for texte, dictionnaire in zip(liste_textes, liste_dictionnaire):
        if mot_recherche in dictionnaire:
            print(mot_recherche, " est présent dans", texte)

            if dictionnaire[mot_recherche] > nb_max:
                nb_max = dictionnaire[mot_recherche]
                texte_max = texte

    if texte_max:
        print(mot_recherche, " est le plus répété dans", texte_max, " ( nombre de répétitions : ", nb_max, ").")
    else:
        print(mot_recherche, " n'a été trouvé dans aucun texte.")
#5



#6

def MotsUtiliséParToutLesPresidents():
    ListMotsOmnipresent = list(ListeDicoTFtextes[0].keys())

    for texte in range(1, len(ListeDicoTFtextes)):
        motsASupprimer = []
        for mot in ListMotsOmnipresent:
            if mot not in ListeDicoTFtextes[texte] or mot in ListMotsPasImportant:
                motsASupprimer.append(mot)
        for mot in motsASupprimer:
            ListMotsOmnipresent.remove(mot)
    print(ListMotsOmnipresent)
