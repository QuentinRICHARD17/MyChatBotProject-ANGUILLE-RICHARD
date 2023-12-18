from math import sqrt
def produitScalaire(matriceTexte, vecteurQuestion):

    ProduitScalaire = [[]]

    # Parcourir la matrice texte pour calculer produit scalaire avec vecteur
    for i in range(1, len(matriceTexte)):
        somme = 0
        ProduitScalaire[0].append(i)
        for j in range(1, len(matriceTexte[i])):
            somme += matriceTexte[i][j] * vecteurQuestion[j]
        ProduitScalaire.append(somme)

    return ProduitScalaire



def NormeVecteurMatrice(Matrice):

    normesVecteurs = [[]]

    # Parcourir lignes matrice, réinitialiser somme_carres et ajouter numero texte a normesVecteur[0]
    for i in range(1, len(Matrice)):
        somme_carres = 0
        normesVecteurs[0].append(i)

        # Parcourir valeurs matrice, faire calcul somme puis norme
        for j in range(1, len(Matrice[i])):
            somme_carres += Matrice[i][j] ** 2
        norme = sqrt(somme_carres)
        normesVecteurs.append(norme)

    '''
    # Afficher liste normes vecteurs texte
    print(normesVecteurs[0])
    for val in range(1, len(normesVecteurs)):
        print(normesVecteurs[val], end=' ')
    '''

    return normesVecteurs



def NormeVecteurQuestion(vecteurQuestion):

    somme_carres = 0

    for i in range(1, len(vecteurQuestion)):
        somme_carres += vecteurQuestion[i] ** 2

    norme = sqrt(somme_carres)

    return norme




def CalculSimilarite(matriceTexte, vecteurQuestion):

    listeScoreSimilarite = [[]]

    produitScalaireMatriceQuestion = produitScalaire(matriceTexte, vecteurQuestion)
    normesVecteursMatrice = NormeVecteurMatrice(matriceTexte)
    normesVecteurQuestion = NormeVecteurQuestion(vecteurQuestion)

    for i in range(1, len(produitScalaireMatriceQuestion)):
        listeScoreSimilarite[0].append(i)
        listeScoreSimilarite.append(produitScalaireMatriceQuestion[i]/(normesVecteursMatrice[i] * normesVecteurQuestion))

    return listeScoreSimilarite




def documentLePlusPertinent(matriceTexte, vecteurQuestion, listeNomFichier):

    listeScoreSimilarite = CalculSimilarite(matriceTexte, vecteurQuestion)

    # Trouver plus grand score similarité
    IndiceDocumentPertinent = listeScoreSimilarite[1:].index(max(listeScoreSimilarite[1:]))
    DocumentLePluspertinent = listeNomFichier[IndiceDocumentPertinent - 1]

    return DocumentLePluspertinent










