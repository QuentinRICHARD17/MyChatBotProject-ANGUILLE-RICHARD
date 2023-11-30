import string
def ConvertionDesMajEnMin(chemin_entree, chemin_sortie):
    # Ouvrir le fichier en lecture
    with open(chemin_entree, 'r', encoding='utf-8') as fichier_entree:
        contenu = fichier_entree.read()

        # Convertir le contenu en minuscules avec la fonction lower
        contenu_en_minuscules = contenu.lower()

        # Supprimer les caractères de ponctuation et gérer les espaces
        contenu_propre = SuppressionPonctuationEtEspaces(contenu_en_minuscules)

        # Ouvrir le fichier en écriture et écrire le contenu converti
        with open(chemin_sortie, 'w', encoding='utf-8') as fichier_sortie:
            fichier_sortie.write(contenu_propre)
            fichier_sortie.write(" ")

def SuppressionPonctuationEtEspaces(MonContenuMinuscule):
    # Créer une chaîne de caractères contenant tous les caractères de ponctuation à supprimer grâce a la bibliothèque string qui fournit une chaîne prédéfinie punctuation qui contient ces caractères.
    caracteres_ponctuation = string.punctuation

    # Remplacer chaque caractère de ponctuation par un espace
    for caractere in caracteres_ponctuation:
        MonContenuMinuscule = MonContenuMinuscule.replace(caractere, ' ')

    #On remplace les espaces quand il y en a par un seul espace
    mots = MonContenuMinuscule.split()
    MonContenuMinuscule = ' '.join(mots)

    return MonContenuMinuscule
