from FonctionsCalculSimilarité import documentLePlusPertinent
from NotreLibrairie import directory
def TF_IDFquestionLePlusEleve(vecteurQuestion):

    indice = vecteurQuestion[1:].index(max(vecteurQuestion[1:]))
    MotTF_IDFlePlusEleve = vecteurQuestion[0][indice]

    return MotTF_IDFlePlusEleve



def generationReponses(matriceTexte, vecteurQuestion, listeNomFichier):

    # Recuperer mot le plus important et document le plus pertinent
    mot = TF_IDFquestionLePlusEleve(vecteurQuestion)
    documentPertinent = documentLePlusPertinent(matriceTexte, vecteurQuestion, listeNomFichier)

    with open(directory + documentPertinent, 'r', encoding = 'utf-8') as f:
        textePertinent = f.read()

    # Lister les phrases du texte
    phrases = textePertinent.split('.')

    # Parcourir les phrases pour trouver le mot et retourner la phrase le contenant
    for phrase in phrases:
        if mot.lower() in phrase.lower():
            return phrase

    return "Aucune phrase n'a été trouvé avec le mot recherché"




def MettreAme(ListeQuestion, reponse):
    question_starters = {
        "comment": "Après analyse, ",
        "pourquoi": "Car, ",
        "peux-tu": "Oui, bien sûr!"
    }
    for i in ListeQuestion:
        if i in question_starters.keys():
            MotDebut = question_starters[i]
            print(MotDebut + reponse)











