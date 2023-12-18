from FonctionsTraitementTextes import *
from FonctionsExtractionNomsPresidents import *
#1
def AfficherMotsLesMoinsImportants(DictionnaireIDF, MatriceTF_IDF):

    motsPasImportants = []
    indice = 0

    # Parcourir les mots du dictionnaire IDF
    for mot in DictionnaireIDF.keys():
        compteur = 0

        # Vérifier si le mot a un TF-IDF nul dans tous les fichiers
        for i in range(len(MatriceTF_IDF[indice])):
            if MatriceTF_IDF[indice][i] == 0.0:
                compteur += 1
        if compteur == len(MatriceTF_IDF[i]):
            motsPasImportants.append(mot)
        indice += 1

    return motsPasImportants



#2

def AfficherMotsAvecScoreTF_IDFLePlusHaut(DictionnaireIDF, MatriceTF_IDF):

    ScoreLePlusHaut = 0
    indice = 0

    for mot, IDF in DictionnaireIDF.items():

        # Vérifier si le mot a un TF-IDF plus élevé que l'actuel score le plus haut
        for i in range(len(MatriceTF_IDF[indice])):
            if MatriceTF_IDF[indice][i] > ScoreLePlusHaut:
                ScoreLePlusHaut = MatriceTF_IDF[indice][i]
                motIDF = mot
        indice += 1

    return motIDF

#3

def AfficheMotLePlusRepeteParUnPresident(nom):
    L = []
    DCP = False  # Variable pour indiquer si le nom a été trouvé

    for i in range(len(files_names)):
        if nom in files_names[i]:
            DCP = True  # Le nom a été trouvé
            L.append(i)

    if not DCP:
        print("Il n'y a pas de document qui porte le nom de", nom)
        return

    print("Le(s) mot(s) le(s) plus répété(s) par", nom, "est(sont):")
    for j in range(len(L)):
        KeyMaxVal = max(ListeDicoTFtextes[L[j]], key=ListeDicoTFtextes[L[j]].get)
        for cle, valeur in ListeDicoTFtextes[L[j]].items():
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
compteur = 0
def ParlerEcologieEtClimat(FichierEntree):
    global compteur
    mot1 = "écologie"
    mot2 = "climat"
    if compteur == 0:
        with open(FichierEntree, 'r', encoding='utf-8') as f:
            contenu = f.read()
            if mot1 in contenu or mot2 in contenu:
                compteur += 1
            if compteur == 1:
                print("Le premier texte à parler du climat/écologie est celui de :", FichierEntree)

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
