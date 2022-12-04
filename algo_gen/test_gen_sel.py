
from RotTable import RotTable
from algo_gen.algo_gen import Algo_gen


def test_generate():
    Rot_table = RotTable()
    Rot_table.generate()
    matrice=Rot_table.getRotTable()
    #verification que l'on récupère une matrice de la bonne taille
    assert len(matrice) == 16

    for dinucleotide in matrice:
        wedge = matrice[dinucleotide][1]
        twist = matrice[dinucleotide][0]
        direction = matrice[dinucleotide][2]
        marge_wedge = Rot_table.get_origin()[dinucleotide][4]
        marge_twist =Rot_table.get_origin()[dinucleotide][3]
        wedge_ini = Rot_table.get_origin()[dinucleotide][1]
        twist_ini = Rot_table.get_origin()[dinucleotide][0]
        direction_ini = Rot_table.get_origin()[dinucleotide][2]
        #vérification que les intervalles sont respéctés
        assert direction == direction_ini
        assert twist >= twist_ini-marge_twist
        assert twist <= twist_ini+marge_twist
        assert wedge >= wedge_ini-marge_wedge and wedge <= wedge_ini+marge_wedge

    pairs = Rot_table.pairs
    for dinucleotide in pairs:
        if pairs[dinucleotide]!=0:
            #vérification que les symétries sont respectées
            assert matrice[dinucleotide][0] == matrice[pairs[dinucleotide]][0]
            assert matrice[dinucleotide][1] == matrice[pairs[dinucleotide]][1]
            assert matrice[dinucleotide][2] == -matrice[pairs[dinucleotide]][2]

def test_selection():
    lineList = [line.rstrip('\n') for line in open('plasmid_8k.fasta')]
    seq = ''.join(lineList[1:])
    algo_bis=Algo_gen(seq,3,2)
    algo_bis.selection()
    new_population_bis=algo_bis.population
    #vérification que la selection se fait bien sur une population impaire
    assert len(new_population_bis)==1
