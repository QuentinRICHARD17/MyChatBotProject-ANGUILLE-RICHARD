from ConvertirMajusculesEnMinusculesEtSupprimerPonctuation import *
from FonctionTFAfficherOccurencesMots import CalculScoreTF
from FonctionExtraireNomsPresidents import *
from FonctionIDF import *
from math import log
from NotreLibrairie import *
from FonctionMatriceTF_IDF import *
from Fonctionnalite import *
from FonctionAssocierPrenomsEtAfficher import *

# Utilisation

files_names = list_of_files(directory, "txt")
print("Listes des noms des textes :")
print(files_names)
print()
print("Listes des noms des Présidents :")
AfficherNomsPresidents()
print()

for i in range(len(files_names)):
    ConvertionDesMajEnMin(directory + files_names[i], CleanedDirectory + files_names[i])
    CalculScoreTF(CleanedDirectory + files_names[i])
CalculScoreIDF()
print("La Matrice :")
CalculMatriceTF_IDF()
print()
print("Fonctionalité n°1 Mots les moins importants :")
AfficherMotsLesMoinsImportants()
print()
print("Fonctionalité n°2 Mots le score TF-IDF le plus haut :")
AfficherMotsAvecScoreTF_IDFLePlusHaut()
print()
print("Fonctionalité n°3 Mots le plus répétéer par le président Chirac : :")
AfficheMotLePlusRepeteParUnPresident(input("Pour quel nom de président voulez vous connaitre quel mot a été répété le plus de fois:"))
print()
print("Fonctionalité n°4 Noms des présidents qui ont parlé de nation ainsi que de celui qui l'a répété le plus de fois :")
ExtraireMotFrequent(files_names, MaListeDeDico)