from math import log
def TFquestion(listeMotsQuestionDansCorpus):

    DicoScoreTFquestion = {}

    for mot in listeMotsQuestionDansCorpus:
        if listeMotsQuestionDansCorpus[mot] in DicoScoreTFquestion:
            DicoScoreTFquestion[mot] += 1
        else:
            DicoScoreTFquestion[mot] = 1

    return DicoScoreTFquestion



def IDFquestion(DicoScoreTFquestion):

    DicoIDF = {}

    for cle in DicoScoreTFquestion.keys():
        if cle in DicoIDF:
            DicoIDF[cle] += 1
        else:
            DicoIDF[cle] = 1
    for mot , occurence in DicoIDF.items():
        DicoIDF[mot] = log(len(DicoScoreTFquestion)/occurence)




