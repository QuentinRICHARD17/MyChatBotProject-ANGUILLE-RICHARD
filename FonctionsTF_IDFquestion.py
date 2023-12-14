def TFquestion(listeMotsQuestionDansCorpus):

    DicoTFquestion = {}

    for mot in listeMotsQuestionDansCorpus:
        if mot in DicoTFquestion:
            DicoTFquestion[mot] += 1
        else:
            DicoTFquestion[mot] = 1
    for mot, val in DicoTFquestion.items():
        DicoTFquestion[mot] /= 10

    return DicoTFquestion



def MatriceTF_IDFquestion(DicoTFquestion, matriceTransposee):

    matriceTF_IDFquestion = matriceTransposee

    # On parcourt la matrice transposée en mettant des 0 si le mot n'est pas dans la question et en multipliant le score IDF par le score TF du mot de la question si le mot est bien dans la question
    for i in range(1, len(matriceTF_IDFquestion)):
        for j in range(1, len(matriceTF_IDFquestion[i])):
            if matriceTF_IDFquestion[0][j] not in DicoTFquestion:
                matriceTF_IDFquestion[i][j] = 0
            else:
                matriceTF_IDFquestion[i][j] = matriceTransposee[i][j] * DicoTFquestion[matriceTF_IDFquestion[0][j]]

    return matriceTF_IDFquestion









