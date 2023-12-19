from Fonctionnalité import *
from FonctionsTF_IDFtextes import *
from FonctionsTraitementQuestion import *
from FonctionsTF_IDFquestion import *
from FonctionsCalculSimilarité import *
from FonctionsGenerationReponses import *


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
DictionnaireIDF = CalculScoreIDF(ListeDicoTFtextes)
print("La Matrice :")
matriceTF_IDF = CalculMatriceTF_IDF(DictionnaireIDF, ListeDicoTFtextes)
print()
matriceTransposee = TransposeeMatriceTF_IDF(matriceTF_IDF)
print("Fonctionalité n°1 Mots les moins importants :")
AfficherMotsLesMoinsImportants(matriceTF_IDF)
print()
print("Fonctionalité n°2 Mots avec le score TF-IDF le plus haut :")
AfficherMotsAvecScoreTF_IDFLePlusHaut(matriceTF_IDF)
print()
print("Fonctionalité n°3 Mots le plus répétéer par le président de votre choix : ")
AfficheMotLePlusRepeteParUnPresident(input("Pour quel nom de président voulez vous connaitre quel mot a été répété le plus de fois :"))
print()
print("Fonctionalité n°4 Noms des présidents qui ont parlé de nation ainsi que de celui qui l'a répété le plus de fois :")
ExtraireMotFrequent(files_names, ListeDicoTFtextes)
print()
print("Fonctionalité n°5 Indiquer le premier président à parler du climat et/ou de l’écologie:")
for x in range(len(files_names)):
    ParlerEcologieEtClimat(CleanedDirectory + files_names[x])
print()
print("Fonctionnalité n°6 le(s) mot(s) que tous les présidents ont évoqués (Hormis les mots dits « non importants ») :")
MotsUtiliséParToutLesPresidents()
print()
questionTokenise = TokenisationQuestion(input("Quel est votre question ?:"))
print()
listeMotsQuestionDansCorpus = IdentificationMotsQuestionDocuments(questionTokenise, ListeDicoTFtextes)
print("Mots de la question qui sont dans le corpus de document :")
print(listeMotsQuestionDansCorpus)
print()
DicoTFquestion = TFquestion(listeMotsQuestionDansCorpus)
vecteurQuestion = vecteurTF_IDFquestion(DicoTFquestion, DictionnaireIDF)
produitScalaire(matriceTransposee, vecteurQuestion)
NormeVecteurMatrice(matriceTransposee)
NormeVecteurQuestion(vecteurQuestion)
CalculSimilarite(matriceTransposee, vecteurQuestion)
documentLePlusPertinent(matriceTransposee, vecteurQuestion, files_names)
TF_IDFquestionLePlusEleve(vecteurQuestion)
reponse = generationReponses(matriceTransposee, vecteurQuestion, files_names)
print(MettreAme(questionTokenise, reponse))








