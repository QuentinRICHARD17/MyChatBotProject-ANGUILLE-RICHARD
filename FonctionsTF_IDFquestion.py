def TFquestion(listeMotsQuestionDansCorpus):

    DicoTFquestion = {}

    for mot in listeMotsQuestionDansCorpus:
        if mot in DicoTFquestion:
            DicoTFquestion[mot] += 1
        else:
            DicoTFquestion[mot] = 1

    return DicoTFquestion



def vecteurTF_IDFquestion(DicoTFquestion, DicoIDF):

    vecteurQuestion = [[]]

    for mot, IDF in DicoIDF.items():
        vecteurQuestion[0].append(mot)
        if mot in DicoTFquestion:
            vecteurQuestion.append(IDF * DicoTFquestion[mot])
        else:
            vecteurQuestion.append(0)
    '''
    # Afficher vecteur
    print(vecteurQuestion[0])
    for val in range(1, len(vecteurQuestion)):
        print(vecteurQuestion[val], end = ' ')
    '''
    return vecteurQuestion








