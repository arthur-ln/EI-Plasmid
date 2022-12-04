from individu import Individu
from population import Population
import math
from random import randint
from evaluation import Evaluation


class Algo_gen:

    def __init__(self, seq, N, T):
        '''
        seq : Séquence de nucléotides, type = string
        N : Taille initiale de la population d'individus, type = int
        T : Nombre de passages dans le cycle de l'algorithme, type = int
        '''
        self.Pop = Population(N)
        self.population = self.Pop.population
        self.seq = seq
        self.N = N
        self.T=T

    def croisement_global(self):
        '''
        Notons n le nombre d'individus de la population.
        Chaque parent engendre un enfant avec un individu aléatoire
        On souhaite obtenir de nouveau le nombre d'individus avant la selection, on rajoute un individu si la population initiales était impaire
        '''
        n = len(self.population)
        for i in range(n//2):
            parent1, parent2 = self.population[i], Individu()
            enfant1, enfant2 = parent1.croisement(parent2)
            self.population.append(enfant1)
            self.population.append(enfant2)
        if n % 2 == 1:
            indiv1 = Individu()
            self.population.append(indiv1)
        if self.N%2!=0:
            indiv2 = Individu()
            self.population.append(indiv2)


    def mutation_globale(self):
        '''
        On applique la fonction mutation à chaque individu sauf le meilleur actuel
        '''

        n = len(self.population)
        indice_min=self.get_min()[0]
        matrice=self.population[indice_min].Rot_table.getRotTable()
        for k in range(n):
                self.population[k].mutation()
        self.population[indice_min].Rot_table.writeRotTable(matrice)

    def get_min(self):
        '''
        permet d'obtenir diverses informations sur l'individu qui a le plus petit score actuel
        '''

        min = math.inf
        for k in range(self.N):
            evaluation = Evaluation(self.seq, self.population[k])
            result = evaluation.result

            if result < min:
                min = result
                indice_min = k
                result_final=result
                distance=evaluation.distance
        return indice_min, result_final, distance

    def get_max(self):
        '''
        permet d'obtenir diverses informations sur l'individu qui a le plus grand score actuel
        '''
        max = 0
        for k in range(self.N):
            evaluation = Evaluation(self.seq, self.population[k])
            result = evaluation.result

            if result > max:
                max = result
                indice_max = k
                result_final=result
                distance=evaluation.distance
        return indice_max, result_final, distance

    def selection(self):  # on peut penser à implémenter une proba de faire gagner le perdent initial
        '''
        On réalise une sélection par tournoi. Notons N la taille de la population avant sélection.
        Si N impair : on enlève le moins bon pour avoir un nombre pair
        Puis on fait se rencontrer les individus 2 par 2 de manière aléatoire et on garde le meilleur score à chaque fois
        '''
        new_population = []

        if self.N % 2 != 0:  # si impair on enlève le plus mauvais et on fait combattre les autres
            indice_max=self.get_max()[0]
            del self.population[indice_max]

        while len(self.population) > 0:

            length = len(self.population)
            indice_0 = 0
            indice_1 = randint(1, length-1)
            eval_0 = Evaluation(self.seq, self.population[indice_0])
            eval_1 = Evaluation(self.seq, self.population[indice_1])
            result_0 = eval_0.result
            result_1 = eval_1.result

            if result_0 >= result_1:
                winner = indice_1
                loser = indice_0
            else:
                winner = indice_0
                loser = indice_1


            new_population.append(self.population[winner])

            #les supprimer en meme temps, or si l'on en supprime un, l'indice de l'autre est donc décallé

            if winner==0:
                del self.population[winner]
                del self.population[loser-1]

            else:
                del self.population[loser]
                del self.population[winner-1]

        self.population = new_population[:]




    def cycle_gen(self):
        '''Correspond à un cycle de l'algorithme'''
        self.selection()
        self.croisement_global()
        self.mutation_globale()
        #lscore = [Evaluation(self.seq,individu).result for individu in self.population] #permet de visualiser l'évolution des scores
        #print(sorted(lscore))

    def boucle__gen(self):
        '''Boucle qui réalise T cycles de l'algorithme'''
        for k in range(self.T):
            self.cycle_gen()

        minimum=self.get_min()
        maximum=self.get_max()
        self.indice_min=minimum[0]
        self.indice_max=maximum[0]
        self.worst_result=maximum[1]
        self.best_result=minimum[1]
        self.best_distance=minimum[2]
        self.pop_score=[]
        for k in range(len(self.population)):
            evaluation=Evaluation(self.seq, self.population[k])
            self.pop_score.append(evaluation.result)
        self.best_individu=self.population[self.indice_min]



