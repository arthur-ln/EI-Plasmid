"""
Fichier définissant la classe représentant un algorithme génétique.
On cherchera toujours à maximiser la fonction et non minimiser.
"""
from random import *
import numpy as np

from individual_vector import Individual_vector

class AlgoGen:

    def __init__(self, Indiv, pop_size, fitness_function, shape, mutation_rate, crossover_rate, starting_interval=None):
        """
        --------
        Fonction appelée à la création d'une instance de la classe.

        On y définit les différents attributs de cette instance et on les initialise.        

        --------
        Paramètres:

        self : instance de la classe AlgoGen.
        Indiv : classe des individus (Individual_vector ou Individual_path) fonctionne comme une fonction ie : Indiv(shape, fitness_function, starting_interval) 
        -> renvoie un individu créer selon votre fonction __init__ de la classe en question.
        pop_size : entier, nombre d'individu constituant la population.
        fitness_function : fonction, fonction que l'on cherche à maximiser.
        shape : entier, taille des chromosomes des individus (taille du vecteur ou ensemble de la permutation [0; shape[).
        mutation_rate : float, [0;1] module la proportion de la population qui va être muté.
        crossover_rate : float, [0;1] module la proportion de la population qui se reproduit.
        starting_interval : float.


        --------
        Return:

        None : Ne renvoie rien.

        """

        self.pop_size = pop_size

        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

        # Generate initial population
        self.population = [Individual_vector(
            shape, fitness_function, starting_interval) for _ in range(pop_size)]

        population = self.population
        population.sort(key=lambda indiv: indiv.fitness_score)
        self.best_indv = population[-1]

        self.actual_pop_size = pop_size

    def parents_selection(self):
        """
        Fonction appelé avec chaque crossover elle renvoie les deux parents qui effecturont le crossover.

         --------
        Paramètres:

        self : instance de la classe AlgoGen, elle possède donc tous les attributs définis dans la fonction __init__().


        --------
        Return:

        Tuple : Un couple d'individus correspondant aux parents que l'on va faire reproduire
        (Syntaxe pour renvoyer un tuple : return parent1, parent2).

        """
        n = self.pop_size
        k = int(0.1*n)
        k_individus = sample(self.population, k)
        k_individus.sort(key=lambda indiv: indiv.fitness_score)
        return(k_individus[-1], k_individus[-2])

    def survivor_selection(self):
        """
        Fonction appelé à la fin de chaque génération. Elle permet de garder la taille de la population constante
        à chaque début d'époque (step / génération).

        --------
        Paramètres:

        self : instance de la classe AlgoGen, elle possède donc tous les attributs définis dans la fonction __init__().


        --------
        Return:

        None : Ne renvoie rien, modifie la population sur place.

        """
        self.population = self.population.sort(
            key=lambda indiv: indiv.fitness_score)
        k = self.actual_pop_size - self.pop_size
        for i in range(k):
            self.population.pop(-1)

    def step(self):
        """
        Fonction simulant un pas de l'algorithme pour passer à la génération suivante.

        --------
        Paramètres:

        self : instance de la classe AlgoGen, elle possède donc tous les attributs définis dans la fonction __init__().


        --------
        Return:

        None : Ne renvoie rien.

        """

        # Crossover
        for i in range(int(self.pop_size*self.crossover_rate)):
            parent1, parent2 = self.parents_selection()
            enfant1, enfant2 = Individual_vector.crossover(parent1, parent2)
            self.population.append(enfant1)
            self.population.append(enfant2)
            self.actual_pop_size = self.actual_pop_size + 2

        # Mutation

        n = self.actual_pop_size
        L = []
        for i in range(n):
            if self.mutation_rate > random():
                L.append(i)
        for x in L:
            Individual_vector.mutate(
                self.population[x], self.population[randint(0, n-1)])

        # Selection des survivants

        self.survivor_selection()
