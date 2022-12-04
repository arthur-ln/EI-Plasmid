from evaluation import Evaluation
from individu import Individu

def test_evaluation():
    lineList = [line.rstrip('\n') for line in open('plasmid_8k.fasta')]
    seq = ''.join(lineList[1:])
    individu=Individu()
    evaluation=Evaluation(seq, individu)
    #vérification que l'on récupère une score positif
    assert evaluation.result>=0
