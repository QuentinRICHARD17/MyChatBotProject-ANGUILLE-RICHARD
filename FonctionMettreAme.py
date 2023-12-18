def MettreAme(ListeQuestion):
    question_starters = {
        "comment": "Après analyse, ",
        "pourquoi": "Car, ",
        "peux-tu": "Oui, bien sûr!"
    }
    for i in ListeQuestion:
        if i in question_starters.keys():
            MotDebut = question_starters[i]
            print(MotDebut, "+réponse à ta question ")

# pour test
MaListeQuestion = ['comment', 'hulk', 'help']
MettreAme(MaListeQuestion)
