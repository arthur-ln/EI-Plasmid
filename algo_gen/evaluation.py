from Traj3D import Traj3D
import math


class Evaluation:

    '''
    fonction d'évaluation qui indique si l'individu est bon ou mauvais
    On prend en compte la distance des extrémités, le nombre d'angle critique (inférieur à 12pi/13) entre chaque dinucléotide ainsi que
    la colinéarité des deux vecteurs aux extrémités

    On cherche à minimiser cette focntion
    '''

    def __init__(self, seq, individu):
        self.seq = seq
        self.individu = individu
        self.Rot_table=self.individu.Rot_table
        self.traj = Traj3D()
        self.traj.compute(self.seq, self.Rot_table)
        self.Lvec = self.traj.getTraj()
        self.nb_mv_angles = 0

        Lp = self.Lvec[-1]     #vecteur en bout de chaine
        Fp = self.Lvec[0]      #vecteur initial

        Lp1 = self.Lvec[-2]   #avant-dernier vecteur
        Fp1 = self.Lvec[1]    #deuxième vecteur


        self.distance = self.norme(Lp-Fp)

        self.angle_i_f=self.angle_aligne(Fp-Fp1,Lp1-Lp)

        self.angle_ext_inf=1/(1+self.angle_i_f)     #angle entre le vecteur initial et final

        #self.angle()

        self.result = self.distance + self.angle_ext_inf #+self.nb_mv_angles/100


    def angle(self):
        '''
        calcul l'angle entre dexu vecteurs consécutifs
        '''
        for i in range(len(self.Lvec)-2):
            vec1 = (self.Lvec[i][0]-self.Lvec[i+1][0], self.Lvec[i][1] -
                    self.Lvec[i+1][1], self.Lvec[i][2]-self.Lvec[i+1][2])
            vec2 = (self.Lvec[i+2][0]-self.Lvec[i+1][0], self.Lvec[i+2][1] -
                    self.Lvec[i+1][1], self.Lvec[i+2][2]-self.Lvec[i+1][2])

            PS = vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2]

            angle0=round(PS/(self.norme(vec1)*self.norme(vec2)),7)

            angle = math.acos(angle0)

            if angle < 12*math.pi/13:
                self.nb_mv_angles += 1



    def norme(self, vec):
        '''
        calcul la norme d'un vecteur
        '''
        return (vec[0]**2+vec[1]**2+vec[2]**2)**0.5


    def angle_aligne(self, vec1, vec2):
        '''
        renvoie le produit scalaire en valeur absolue de deux vecteurs
        '''
        produit_s = vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2]
        return abs(produit_s)
