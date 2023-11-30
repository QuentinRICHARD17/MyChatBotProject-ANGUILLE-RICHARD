from FonctionMatriceTF_IDF import *
from FonctionTFAfficherOccurencesMots import *
from FonctionIDF import *
from FonctionAssocierPrenomsEtAfficher import *
#1
def AfficherMotsLesMoinsImportants():
    L = []
    for i in range(1, len(MatriceTF_IDF)):
        compteur = 0
        for j in range(1, len(MatriceTF_IDF[i])):
            if MatriceTF_IDF[i][j] != 0.0:
                compteur += 1
        if compteur == 0:
            L.append(MatriceTF_IDF[i][0])
    print("Les mots les moins importants du dossier sont:", end=' ')
    for k in range(len(L) - 1):
        print(L[k], ",", end=' ')
    print(L[k + 1])

#2

def AfficherMotsAvecScoreTF_IDFLePlusHaut():
    ScoreLePlusHaut = 0
    for i in range(1 , len(MatriceTF_IDF)):
        for j in range(1, len(MatriceTF_IDF[i])):
            if MatriceTF_IDF[i][j] >= ScoreLePlusHaut:
                ScoreLePlusHaut = MatriceTF_IDF[i][j]
    print("Les mots ayant le score TF-IDF le plus élevé sont:", end=' ')
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

    print("Le(s) mot(s) le(s) plus répété(s) par", nom, "sont:")
    for j in range(len(L)):
        KeyMaxVal = max(MaListeDeDico[L[j]] , key = MaListeDeDico[L[j]].get)
        for cle , valeur in MaListeDeDico[L[j]].items():
            if valeur == MaListeDeDico[L[j]][KeyMaxVal]:
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
'''
def MotsUtiliséParToutLesPresidents():
    
'''







