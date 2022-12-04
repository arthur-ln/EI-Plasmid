from Traj3D import Traj3D
from RotTable import RotTable
import math


class Evaluation:

    def __init__(self, seq, table_dict):
        self.seq = seq
        self.rot_table = RotTable()
        self.rot_table.writeRotTable(table_dict)
        self.traj = Traj3D()
        self.traj.compute(self.seq, self.rot_table)
        self.Lvec = self.traj.getTraj()
        self.nb_mv_angles = 0

        Lp = self.Lvec[-1]
        Fp = self.Lvec[0]

        Lp1 = self.Lvec[-2]  # avant-dernier vecteur
        Fp1 = self.Lvec[1]  # deuxième vecteur

        self.distance = self.norme(Lp-Fp)

        self.angle_i_f = self.angle_aligne(Fp-Fp1, Lp1-Lp)

        # angle entre le vecteur initial et final
        self.angle_ext_inf = 1/(1+self.angle_i_f)

        # self.angle()

        self.result = self.distance + self.angle_ext_inf  # +self.nb_mv_angles/100

    def angle(self):
        for i in range(len(self.Lvec)-2):
            vec1 = (self.Lvec[i][0]-self.Lvec[i+1][0], self.Lvec[i][1] -
                    self.Lvec[i+1][1], self.Lvec[i][2]-self.Lvec[i+1][2])
            vec2 = (self.Lvec[i+2][0]-self.Lvec[i+1][0], self.Lvec[i+2][1] -
                    self.Lvec[i+1][1], self.Lvec[i+2][2]-self.Lvec[i+1][2])

            PS = round(vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2], 7)
            try:
                angle = math.acos(PS/(self.norme(vec1)*self.norme(vec2)))
            except ValueError:
                return math.pi

            if angle < 2*math.pi/3:
                self.nb_mv_angles += 1

    def norme(self, vec):
        return (vec[0]**2+vec[1]**2+vec[2]**2)**0.5

    def angle_aligne(self, vec1, vec2):
        '''
        renvoie le produit scalaire en valeur absolue de deux vecteurs
        '''
        produit_s = vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2]
        return abs(produit_s)
