from individu import Individu


class Population:

    def __init__(self, N):
        self.population = []
        for k in range(N):
            individu=Individu()
            self.individu=individu
            self.population.append(individu)