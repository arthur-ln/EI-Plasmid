from RotTable import RotTable
import numpy.random as rd


class Individu:

    def __init__(self):
        self.Rot_table=RotTable()
        self.Rot_table.generate()
        self.pairs=self.Rot_table.pairs
        self.alpha = 0.001
        self.beta = 0.01


    def croisement(self, individu2):
        '''
        Méthode de découpage:
            Enfant1 partage avec Parent1 : AA,TT;AC,GT;AG,CT et CG;GC
                            avec Parent2 : CA,TG;CC,GG;GA,TC et TA;AT
            Enfant2 partage avec Parent1 : CA,TG;CC,GG;GA,TC et TA;AT
                            avec Parent2 : AA,TT;AC,GT;AG,CT et CG;GC
        '''
        Enfant1 = Individu()
        Enfant2 = Individu()
        Enfant1_Rot_table = Enfant1.Rot_table
        Enfant2_Rot_table = Enfant2.Rot_table
        Parent1_Rot_table = self.Rot_table
        Parent2_Rot_table = individu2.Rot_table

        # Liste qui contient un dinucléotide par paire (s'il y a)
        Liste = list(self.pairs)
        for i in range(3):
            dinucleotide1, dinucleotide2 = Liste[i], self.pairs[Liste[i]]
            Enfant1_Rot_table.writeVector(dinucleotide1, Parent1_Rot_table.getVector(dinucleotide1))
            Enfant1_Rot_table.writeVector(dinucleotide2, Parent1_Rot_table.getVector(dinucleotide2))
            Enfant2_Rot_table.writeVector(dinucleotide1, Parent2_Rot_table.getVector(dinucleotide1))
            Enfant2_Rot_table.writeVector(dinucleotide2, Parent2_Rot_table.getVector(dinucleotide2))
        for i in range(3, 6):
            dinucleotide1, dinucleotide2 = Liste[i], self.pairs[Liste[i]]
            Enfant1_Rot_table.writeVector(dinucleotide1, Parent2_Rot_table.getVector(dinucleotide1))
            Enfant1_Rot_table.writeVector(dinucleotide2, Parent2_Rot_table.getVector(dinucleotide2))
            Enfant2_Rot_table.writeVector(dinucleotide1, Parent1_Rot_table.getVector(dinucleotide1))
            Enfant2_Rot_table.writeVector(dinucleotide2, Parent1_Rot_table.getVector(dinucleotide2))
        for i in range(6, 8):
            dinucleotide = Liste[i]
            Enfant1_Rot_table.writeVector(dinucleotide, Parent1_Rot_table.getVector(dinucleotide))
            Enfant2_Rot_table.writeVector(dinucleotide, Parent2_Rot_table.getVector(dinucleotide))
        for i in range(8, 10):
            dinucleotide = Liste[i]
            Enfant1_Rot_table.writeVector(dinucleotide, Parent2_Rot_table.getVector(dinucleotide))
            Enfant2_Rot_table.writeVector(dinucleotide, Parent1_Rot_table.getVector(dinucleotide))
        return(Enfant1, Enfant2)


    def mutation(self):
        '''
        Chaque gène parmi les 32 (16*2) a une chance Pm de muter sachant que:
            0.001<Pm<0.01 distribué selon une loi uniforme
            Pm varie au cours du temps et change pour chaque gène
        Si un gène mute, on conserve les symétries de la matrice
        '''

        #lp contient les probas Pm de muter pour chaque gène
        lp=[rd.uniform(self.alpha,self.beta) for dinucleotide in self.pairs]+[rd.uniform(self.alpha,self.beta) for dinucleotide in self.pairs]
        k=0

        for dinucleotide in self.pairs:

            int_0_i, int_0_f = self.Rot_table.getTwist(dinucleotide)-self.Rot_table.getTwistInt(
                dinucleotide), self.Rot_table.getTwist(dinucleotide)+self.Rot_table.getTwistInt(dinucleotide)
            int_1_i, int_1_f = self.Rot_table.getWedge(dinucleotide)-self.Rot_table.getWedgeInt(
                dinucleotide), self.Rot_table.getWedge(dinucleotide)+self.Rot_table.getWedgeInt(dinucleotide)
            if rd.binomial(1, lp[k], 1) == [1]:
                twist_value = rd.uniform(int_0_i, int_0_f)
                self.Rot_table.writeTwist(dinucleotide,twist_value)
            k=k+1
            if rd.binomial(1, lp[k], 1) == [1]:
                wedge_value = rd.uniform(int_1_i, int_1_f)
                self.Rot_table.writeWedge(dinucleotide,wedge_value)
            k=k+1
            if self.pairs[dinucleotide] != 0:
                dinucleotide_pair = self.pairs[dinucleotide]
                self.Rot_table.writeTwist(dinucleotide_pair, self.Rot_table.getTwist(dinucleotide))
                self.Rot_table.writeWedge(dinucleotide_pair, self.Rot_table.getWedge(dinucleotide))
