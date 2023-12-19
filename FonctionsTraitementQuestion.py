from FonctionsTraitementTextes import *
import string
from FonctionsTF_IDFtextes import CalculScoreTF

def TokenisationQuestion(question):

    # Convertir le contenu en minuscules avec la fonction lower
    questionEnMinuscule = question.lower()

    # Supprimer les caractères de ponctuation et gérer les espaces
    questionTraite = SuppressionPonctuationEtEspacesQuestion(questionEnMinuscule)

    # Lister les mots de la question
    questionTokenise = questionTraite.split()

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


def IdentificationMotsQuestionDocuments(questionTokenise, ListeDicoTFtextes):

    motsPresent = set()

    for mot in questionTokenise:
        for dico in ListeDicoTFtextes:
            if mot in dico:
                motsPresent.add(mot)

    return list(motsPresent)
