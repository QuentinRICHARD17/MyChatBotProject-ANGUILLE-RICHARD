import math
def NormeVecteurMatrice(MatriceTest):
    CompteurNumVecteur = 0
    for x in MatriceTest:
        somme_carres = 0
        for valeur in x:
            somme_carres += valeur ** 2

        norme = math.sqrt(somme_carres)
        CompteurNumVecteur += 1
        print("vecteur", CompteurNumVecteur, " norme :", norme)

    return norme

def NormeVecteurQuestion(ListeQuestion):
    somme_carres = 0
    for valeur in ListeQuestion:
        somme_carres += valeur ** 2

    norme = math.sqrt(somme_carres)
    print("vecteur norme question :", norme)

    return norme

'''
MaMatriceTest = [[1, 2, 3, 4], 
                 [7, 5, 2, 9], 
                 [5, 8, 2, 6]] 
                 
MaListeQuestion = [4, 5, 2, 1] 

NormeVecteurMatrice(MaMatriceTest)
NormeVecteurQuestion(MaListeQuestion)  
'''