from individu import Individu
from algo_gen.algo_gen import Algo_gen

def test_mutation():
    # Vérif de l'individu
    Indiv1=Individu()
    Indiv1.mutation()

    assert(type(Indiv1)==Individu)
    R1 = Indiv1.Rot_table
    matrice=R1.getRotTable()
    #verif de la taille de la matrice
    assert len(matrice) == 16

    for dinucleotide in matrice:
        wedge = matrice[dinucleotide][1]
        twist = matrice[dinucleotide][0]
        direction = matrice[dinucleotide][2]
        marge_wedge = R1.get_origin()[dinucleotide][4]
        marge_twist =R1.get_origin()[dinucleotide][3]
        wedge_ini = R1.get_origin()[dinucleotide][1]
        twist_ini = R1.get_origin()[dinucleotide][0]
        direction_ini = R1.get_origin()[dinucleotide][2]
        #vérification que les intervalles sont bien respectés
        assert direction == direction_ini
        assert twist >= twist_ini-marge_twist
        assert twist <= twist_ini+marge_twist
        assert wedge >= wedge_ini-marge_wedge and wedge <= wedge_ini+marge_wedge

    pairs = R1.pairs
    for dinucleotide in pairs:
        if pairs[dinucleotide]!=0:
            #vérification que les symétries sont respectées
            assert matrice[dinucleotide][0] == matrice[pairs[dinucleotide]][0]
            assert matrice[dinucleotide][1] == matrice[pairs[dinucleotide]][1]
            assert matrice[dinucleotide][2] == -matrice[pairs[dinucleotide]][2]

def test_mutation_globale():
    lineList = [line.rstrip('\n') for line in open('plasmid_8k.fasta')]
    seq = ''.join(lineList[1:])
    algo=Algo_gen(seq, 4, 2)
    len_before= len(algo.population)
    algo.mutation_globale()
    len_after=len(algo.population)
    #vérification que la mutation n'affecte pas la taille de la population
    assert len_before == len_after
