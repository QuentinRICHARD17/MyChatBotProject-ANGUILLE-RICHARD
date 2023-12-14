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



def MatriceTF_IDFquestion(DicoScoreTFquestion, matriceTransposee):

    for i in range(len(matriceTransposee)):
        for j in range(len(matriceTransposee[i])):
            








