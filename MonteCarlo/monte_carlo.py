import numpy as np


class MonteCarlo:

    # les choses non generiques ici sont seulement l'argument seq
    # Rq: N correspond au nb de simu aléatoire à faire pour évaluer une feuille
    def __init__(self, initial, moveClass, eval, seq, Nb_explo, Nb_simu=5):
        self.initial = initial
        self.tree = {'table': initial, 'children': {}, 'parent': None}
        self.moveClass = moveClass
        self.eval = eval
        self.Nb_simu = Nb_simu
        self.seq = seq
        self.Nb_explo = Nb_explo

    # Créer, à partir d'une config parent, l'ensemble des configurations possibles suivantes

    def gen(self, parent):
        # Créer un dictionnaire avec les fils du parent et qui ont la mm structure
        # {'fils_i':table,'children':{},'parent':parent,'score':None}
        new_gen = self.moveClass(parent).children()

        # Mise à jour des enfants dans la table parent
        parent['children'] = new_gen

        # une fois tous les enfants générés, on met à jour l'arbre gene de tous les enfants
        for enfant in parent['children']:
            parent['children'][enfant]['parent'] = parent

    # Pour trouver quel sommet traiter en fonction du score moyen
    def selection(self):

        # On part de la racine
        current = self.tree

        # Tant que l'on a pas atteint un noeud terminal on
        # parcourt les enfants du sommet en cours de traitement
        while current['children'] != {}:
            min = np.inf
            for enfant in current['children'].keys():
                fils = current['children'][enfant]
                score = fils['score']

                # Si un fils n'a pas été évalué, on le choisit
                if score == None:
                    return fils

                # Sinon on garde celui avec le score le + faible
                if score < min:
                    min = score
                    current = fils
        return current

    def eval_and_update_score(self, node):
        # Si on traite une feuille, son score est determiné à partir de N simus random
        score = node['score']
        if score == None:
            sum_score = 0
            for i in range(self.Nb_simu):
                random_sol = self.moveClass(node).gen_random()
                score_random = self.eval(self.seq, random_sol).result
                sum_score += score_random
            node['score'] = sum_score/self.Nb_simu

        # Si on traite un sommet avec des enfants, on fait la moyenne des scores des enfants
        else:
            sum_score = 0
            Nb_children_eval = 0
            for enfant in node['children']:
                score = node['children'][enfant]['score']
                if score != None:
                    sum_score += score
                    Nb_children_eval += 1

            node['score'] = sum_score/len(node['children'])

        # Tant qu'on est pas à la racine, on remonte l'arbre pour mettre à jour les scores des
        # parents, grand parent etc...
        parent = node['parent']

        # Ne met pas à jour le score de la racine
        if parent['parent'] != None:
            MonteCarlo.eval_and_update_score(self, node['parent'])

    def process(self):

        bestNode = self.tree

        # Crée les premiers enfants de la racine
        MonteCarlo.gen(self, bestNode)

        for i in range(self.Nb_explo):

            # recherche du bestNode
            bestNode = MonteCarlo.selection(self)

            # generation d'enfants pour le bestNode
            MonteCarlo.gen(self, bestNode)

            # eval et MaJ du score de l'arbre
            MonteCarlo.eval_and_update_score(self, bestNode)

        return bestNode
