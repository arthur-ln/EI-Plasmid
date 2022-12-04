from logging.handlers import RotatingFileHandler
import mathutils
import numpy.random as rd
import copy as cp


class RotTable:
    """Represents the rotation table"""

    # 3 first values: 3 angle values
    # 3 last values: SD values
    __ORIGINAL_ROT_TABLE = {\
        "AA": [35.62 , 7.2 , -154 ,      0.06 ,  0.6   , 0],\
        "AC": [34.4  , 1.1 ,  143 ,      1.3  ,  5     , 0],\
        "AG": [27.7  , 8.4 ,    2 ,      1.5  ,  3     , 0],\
        "AT": [31.5  , 2.6 ,    0 ,      1.1  ,  2     , 0],\
        "CA": [34.5  , 3.5 ,  -64 ,      0.9  , 34     , 0],\
        "CC": [33.67 , 2.1 ,  -57 ,      0.07 ,  2.1   , 0],\
        "CG": [29.8  , 6.7 ,    0 ,      1.1  ,  1.5   , 0],\
        "CT": [27.7  , 8.4 ,   -2 ,      1.5  ,  3     , 0],\
        "GA": [36.9  , 5.3 ,  120 ,      0.9  ,  6     , 0],\
        "GC": [40    , 5   ,  180 ,      1.2  ,  1.275 , 0],\
        "GG": [33.67 , 2.1 ,   57 ,      0.07 ,  2.1   , 0],\
        "GT": [34.4  , 1.1 , -143 ,      1.3  ,  5     , 0],\
        "TA": [36    , 0.9 ,    0 ,      1.1  ,  2     , 0],\
        "TC": [36.9  , 5.3 , -120 ,      0.9  ,  6     , 0],\
        "TG": [34.5  , 3.5 ,   64 ,      0.9  , 34     , 0],\
        "TT": [35.62 , 7.2 ,  154 ,      0.06 ,  0.6   , 0]\
        }

    def __init__(self):
        self.__Rot_Table = {}
        for dinucleotide in RotTable.__ORIGINAL_ROT_TABLE:
            self.__Rot_Table[dinucleotide] = RotTable.__ORIGINAL_ROT_TABLE[dinucleotide][:3]
        self.pairs = {"AA": "TT", "AC": "GT", "AG": "CT", "CA": "TG",
                      "CC": "GG", "GA": "TC", "CG": 0, "GC": 0, "TA": 0, "AT": 0}

    ###################
    # WRITING METHODS #
    ###################

    def generate(self):
        '''
        modifie de manière aléatoire les coefficients de la matrice de rotation en restant dans l'intervalle autorisé
         '''

        for dinucleotide in self.pairs:

            int_0_i, int_0_f = self.getTwist(dinucleotide)-self.getTwistInt(
                dinucleotide), self.getTwist(dinucleotide)+self.getTwistInt(dinucleotide)
            int_1_i, int_1_f = self.getWedge(dinucleotide)-self.getWedgeInt(
                dinucleotide), self.getWedge(dinucleotide)+self.getWedgeInt(dinucleotide)

            # Les nouvelles valeurs sont générées selon une loi uniforme sur l'intervalle autorisé
            twist_value = rd.uniform(
                int_0_i, int_0_f)
            wedge_value = rd.uniform(
                int_1_i, int_1_f)

            self.__Rot_Table[dinucleotide][0] = twist_value
            self.__Rot_Table[dinucleotide][1] = wedge_value

            # On garde les symétries de la matrice
            if self.pairs[dinucleotide] != 0:
                dinucleotide_pair = self.pairs[dinucleotide]
                self.__Rot_Table[dinucleotide_pair][0] = twist_value
                self.__Rot_Table[dinucleotide_pair][1] = wedge_value


    def writeRotTable(self,dico):
        self.__Rot_Table = dico

    def writeVector(self,dinucleotide,vecteur):
        self.__Rot_Table[dinucleotide] = vecteur

    def writeTwist(self,dinucleotide,valeur):
        self.__Rot_Table[dinucleotide][0] = valeur

    def writeWedge(self,dinucleotide,valeur):
        self.__Rot_Table[dinucleotide][1] = valeur

    def writeDirection(self,dinucleotide,valeur):
        self.__Rot_Table[dinucleotide][2] = valeur

    ###################
    # READING METHODS #
    ###################

    def getRotTable(self):
        return cp.deepcopy(self.__Rot_Table)

    def getVector(self,dinucleotide):
        return self.__Rot_Table[dinucleotide]

    def getTwist(self, dinucleotide):
        return self.__Rot_Table[dinucleotide][0]

    def getWedge(self, dinucleotide):
        return self.__Rot_Table[dinucleotide][1]

    def getDirection(self, dinucleotide):
        return self.__Rot_Table[dinucleotide][2]

    def getTwistInt(self, dinucleotide):
        return self.__ORIGINAL_ROT_TABLE[dinucleotide][3]

    def getWedgeInt(self, dinucleotide):
        return self.__ORIGINAL_ROT_TABLE[dinucleotide][4]

    def getDirectionInt(self, dinucleotide):
        return self.__ORIGINAL_ROT_TABLE[dinucleotide][5]

    def getTwistOrigin(self, dinucleotide):
        return self.__ORIGINAL_ROT_TABLE[dinucleotide][0]

    def getWedgeOrigin(self, dinucleotide):
        return self.__ORIGINAL_ROT_TABLE[dinucleotide][1]

    def getDirectionOrigin(self, dinucleotide):
        return self.__ORIGINAL_ROT_TABLE[dinucleotide][2]

    def get_origin(self):
        return self.__ORIGINAL_ROT_TABLE
