from RotTable import RotTable
from individu import Individu
from algo_gen.algo_gen import Algo_gen

def test_croisement():
    parent1_indiv = Individu()
    parent1_indiv.Rot_table.generate()
    parent2_indiv = Individu()
    parent2_indiv.Rot_table.generate()

    enfant1_indiv, enfant2_indiv = parent1_indiv.croisement(parent2_indiv)

    parent1 = parent1_indiv.Rot_table
    parent2 = parent2_indiv.Rot_table
    enfant1 = enfant1_indiv.Rot_table
    enfant2 = enfant2_indiv.Rot_table

    # Vérification du bon type
    assert(type(enfant1_indiv) == Individu and type(enfant1_indiv) == Individu)
    assert(type(enfant1) == RotTable and type(enfant2) == RotTable)

    # Vérification symétrie
    for dinucleotide in enfant1.pairs:
        if enfant1.pairs[dinucleotide] != 0:
            dinucleotidesym = enfant1.pairs[dinucleotide]
            assert(enfant1.getTwist(dinucleotide) == enfant1.getTwist(dinucleotidesym))
            assert(enfant1.getWedge(dinucleotide) == enfant1.getWedge(dinucleotidesym))
            assert(enfant2.getTwist(dinucleotide) == enfant2.getTwist(dinucleotidesym))
            assert(enfant2.getWedge(dinucleotide) == enfant2.getWedge(dinucleotidesym))

    # Vérification hérédité des parents
    for dinucleotide in enfant1.getRotTable():
        assert((enfant1.getVector(dinucleotide) == parent1.getVector(dinucleotide)) or (enfant1.getVector(dinucleotide) == parent2.getVector(dinucleotide)))
        assert((enfant2.getVector(dinucleotide) == parent1.getVector(dinucleotide)) or (enfant2.getVector(dinucleotide) == parent2.getVector(dinucleotide)))


def test_croisement_global():
    lineList = [line.rstrip('\n') for line in open('plasmid_8k.fasta')]
    seq = ''.join(lineList[1:])
    algo=Algo_gen(seq,3,2)
    len_before=len(algo.population)
    algo.selection()
    algo.croisement_global()
    len_after=len(algo.population)
    #verification que l'on récupère le même nombre d'individus qu'avant la selection
    assert len_before == len_after

