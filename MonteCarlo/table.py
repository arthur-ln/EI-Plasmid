import copy
import numpy as np


class Table:

    # Parent est un dictionnaire represente un sommet
    # N est le nombre de branche à créer depuis un parent
    def __init__(self, parent, N=10):
        self.N = N
        self.parent = parent
        self.pairs = {"AA": "TT", "AC": "GT", "AG": "CT", "CA": "TG",
                      "CC": "GG", "GA": "TC", "CG": 0, "GC": 0, "TA": 0, "AT": 0}
        self.matching = {0: "AA", 1: "AC", 2: "AG", 3: "CA",
                         4: "CC", 5: "GA", 6: "CG", 7: "GC", 8: "TA", 9: "AT"}

        self.depth = Table.get_depth(self)
        try:
            self.pair = self.matching[self.depth]
        except KeyError:
            self.pair = "AT"

    # Permet de trouver la profondeur d'un noeud, soit le coeff que l'on va modifier
    # (qui sera identifié grâce à la table matching dans le init)
    def get_depth(self):
        depth = 0
        node = copy.deepcopy(self.parent)
        while node['parent'] != None:
            depth += 1
            node = copy.deepcopy(node['parent'])
        return depth

    __ORIGINAL_ROT_TABLE = {
        "AA": [35.62, 7.2, -154,      0.06,  0.6, 0],
        "AC": [34.4, 1.1,  143,      1.3,  5, 0],
        "AG": [27.7, 8.4,    2,      1.5,  3, 0],
        "AT": [31.5, 2.6,    0,      1.1,  2, 0],
        "CA": [34.5, 3.5,  -64,      0.9, 34, 0],
        "CC": [33.67, 2.1,  -57,      0.07,  2.1, 0],
        "CG": [29.8, 6.7,    0,      1.1,  1.5, 0],
        "CT": [27.7, 8.4,   -2,      1.5,  3, 0],
        "GA": [36.9, 5.3,  120,      0.9,  6, 0],
        "GC": [40, 5,  180,      1.2,  1.275, 0],
        "GG": [33.67, 2.1,   57,      0.07,  2.1, 0],
        "GT": [34.4, 1.1, -143,      1.3,  5, 0],
        "TA": [36, 0.9,    0,      1.1,  2, 0],
        "TC": [36.9, 5.3, -120,      0.9,  6, 0],
        "TG": [34.5, 3.5,   64,      0.9, 34, 0],
        "TT": [35.62, 7.2,  154,      0.06,  0.6, 0]}

    def get_original():
        table = dict(Table.__ORIGINAL_ROT_TABLE)
        for pair in table:
            table[pair] = table[pair][:3]
        return table

    def getTwist(self):
        return Table.__ORIGINAL_ROT_TABLE[self.pair][0]

    def getWedge(self):
        return Table.__ORIGINAL_ROT_TABLE[self.pair][1]

    def getTwistInt(self):
        return Table.__ORIGINAL_ROT_TABLE[self.pair][3]

    def getWedgeInt(self):
        return Table.__ORIGINAL_ROT_TABLE[self.pair][4]

    def twist_table(self, i):
        table = copy.deepcopy(self.parent['table'])
        TwistInt = self.getTwistInt()
        table[self.pair][0] = (table[self.pair][0] -
                               TwistInt) + (i/self.N)*2*TwistInt

        associe = self.pairs[self.pair]
        if associe != 0:
            table[associe][0] = table[self.pair][0]

        return table

    def wedge_table(self, i):
        table = copy.deepcopy(self.parent['table'])
        WedgeInt = self.getWedgeInt()
        table[self.pair][1] = (table[self.pair][1] -
                               WedgeInt) + (i/self.N)*2*WedgeInt

        associe = self.pairs[self.pair]
        if associe != 0:
            table[associe][1] = table[self.pair][1]

        return table

    def children(self):
        twist_tree = {'t%d' % i:
                      {'table': Table.twist_table(self, i),
                       'children': {}, 'score': None} for i in range(self.N+1)}
        wedge_tree = {'w%d' % i:
                      {'table': Table.wedge_table(self, i),
                       'children': {}, 'score': None}
                      for i in range(self.N+1)}
        return {**twist_tree, **wedge_tree}

    def gen_random(self):
        table = copy.deepcopy(self.parent['table'])
        gene_a_modif = list(self.pairs.keys())[self.depth:]
        for dinucleotide in gene_a_modif:
            random_twist = np.random.uniform(
                table[dinucleotide][0] -
                Table.__ORIGINAL_ROT_TABLE[dinucleotide][3],
                table[dinucleotide][0]+Table.__ORIGINAL_ROT_TABLE[dinucleotide][3])
            random_wedge = np.random.uniform(
                table[dinucleotide][1] -
                Table.__ORIGINAL_ROT_TABLE[dinucleotide][4],
                table[dinucleotide][1]+Table.__ORIGINAL_ROT_TABLE[dinucleotide][4])
            table[dinucleotide][0] = random_twist
            table[dinucleotide][1] = random_wedge

            associe = self.pairs[dinucleotide]
            if associe != 0:
                table[associe][0] = random_twist
                table[associe][1] = random_wedge
        return table
