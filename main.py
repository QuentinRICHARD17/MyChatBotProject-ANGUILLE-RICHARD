from FonctionsExtractionNomsPresidents import *
from NotreLibrairie import *
from FonctionsTraitementTextes import *
from Fonctionnalité import *
from FonctionsTF_IDFtextes import *
from FonctionsTraitementQuestion import *
from FonctionsTF_IDFquestion import *

# Utilisation

files_names = list_of_files(directory, "txt")
print("Listes des noms des textes :")
print(files_names)
print()
print("Listes des noms des Présidents :")
AfficherNomsPresidents()
print()

for i in range(len(files_names)):
    ConvertionDesMajEnMinTextes(directory + files_names[i], CleanedDirectory + files_names[i])
    CalculScoreTF(CleanedDirectory + files_names[i])
CalculScoreIDF(ListeDicoTFtextes)
print("La Matrice :")
matriceTF_IDF = CalculMatriceTF_IDF()
print()
TransposéMatriceTF_IDF(matriceTF_IDF)

print("Fonctionalité n°1 Mots les moins importants :")
AfficherMotsLesMoinsImportants(MatriceTF_IDF)
print()
print("Fonctionalité n°2 Mots le score TF-IDF le plus haut :")
AfficherMotsAvecScoreTF_IDFLePlusHaut(MatriceTF_IDF)
print()
print("Fonctionalité n°3 Mots le plus répétéer par le président Chirac : ")
AfficheMotLePlusRepeteParUnPresident(input("Pour quel nom de président voulez vous connaitre quel mot a été répété le plus de fois :"))
print()
print("Fonctionalité n°4 Noms des présidents qui ont parlé de nation ainsi que de celui qui l'a répété le plus de fois :")
ExtraireMotFrequent(files_names, ListeDicoTFtextes)
print()
print("Fonctionalité n°5 :")

print("Fonctionnalité n°6 le(s) mot(s) que tous les présidents ont évoqués (Hormis les mots dits « non importants ») :")
MotsUtiliséParToutLesPresidents()
print()
print("Question 1, 2, 3 de la partie  ")
questionTokenise = TokenisationQuestion(input("Quel est votre question ?:"))
listeMotsQuestionDansCorpus = IdentificationMotsQuestionDocuments(questionTokenise, ListeDicoTFtextes)
TFquestion(listeMotsQuestionDansCorpus)
