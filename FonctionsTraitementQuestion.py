from FonctionsTraitementTextes import *
import string
from FonctionsTF_IDFtextes import CalculScoreTF

def TokenisationQuestion(question):

    # Convertir le contenu en minuscules avec la fonction lower
    questionEnMinuscule = question.lower()

    # Supprimer les caractères de ponctuation et gérer les espaces
    questionTraite = SuppressionPonctuationEtEspacesQuestion(questionEnMinuscule)

    # Lister les mots de la question
    questionTokenise = ListerMotsQuestion(questionTraite)

    return questionTokenise


def SuppressionPonctuationEtEspacesQuestion(questionEnMinuscule):

    # Créer une chaîne de caractères contenant tous les caractères de ponctuation à supprimer grâce a la bibliothèque string qui fournit une chaîne prédéfinie punctuation qui contient ces caractères.
    ponctuation = string.punctuation

    # Remplacer chaque caractère de ponctuation par un espace
    for caractere in ponctuation:
        questionEnMinuscule = questionEnMinuscule.replace(caractere, ' ')

    # On remplace les espaces quand il y en a par un seul espace
    mots = questionEnMinuscule.split()
    questionEnMinuscule = ' '.join(mots)

    return questionEnMinuscule


def ListerMotsQuestion(questionTraite):
    listeMotsQuestion = []

    # Initialisation compteur
    i = 0
    j = 0

    # On parcours la question traité a l'aide de 2 compteurs afin de délimiter les mots
    while i < len(questionTraite):
        while i < len(questionTraite) and ord(questionTraite[i]) == 32:
            i += 1
        j = i
        while j < len(questionTraite) and ord(questionTraite[j]) != 32:
            j += 1
        if i < j:
            mot = questionTraite[i:j]
            if mot not in listeMotsQuestion:
                listeMotsQuestion.append(mot)
        i = j + 1

    return listeMotsQuestion


def IdentificationMotsQuestionDocuments(questionTokenise, ListeDicoTFtextes):

    motsPresent = set()

    for mot in questionTokenise:
        for dico in ListeDicoTFtextes:
            if mot in dico:
                motsPresent.add(mot)

    return list(motsPresent)
