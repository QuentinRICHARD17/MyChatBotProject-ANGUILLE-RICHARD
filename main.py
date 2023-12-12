from FonctionsExtractionNomsPresidents import *
from NotreLibrairie import *
from FonctionsTraitementTextes import *
from Fonctionnalité import *
from FonctionsTF_IDFtextes import *
from FonctionsTraitementQuestion import *
from FonctionsTF_IDFquestion import *

# Utilisation

files_names = list_of_files(directory, "txt")
print(files_names)
AfficherNomsPresidents()

for i in range(len(files_names)):
    ConvertionDesMajEnMinTextes(directory + files_names[i], CleanedDirectory + files_names[i])
    CalculScoreTF(CleanedDirectory + files_names[i])
CalculScoreIDF(ListeDicoTFtextes)
matriceTF_IDF = CalculMatriceTF_IDF()
TransposéMatriceTF_IDF(matriceTF_IDF)
AfficherMotsLesMoinsImportants(MatriceTF_IDF)
AfficherMotsAvecScoreTF_IDFLePlusHaut(MatriceTF_IDF)
AfficheMotLePlusRepeteParUnPresident(input("Pour quel nom de président voulez vous connaitre quel mot a été répété le plus de fois:"))
MotsUtiliséParToutLesPresidents()
'''
questionTokenise = TokenisationQuestion(input("Quel est votre question ?:"))
listeMotsQuestionDansCorpus = IdentificationMotsQuestionDocuments(questionTokenise, ListeDicoTFtextes)
TFquestion(listeMotsQuestionDansCorpus)
'''