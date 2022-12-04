from monte_carlo import MonteCarlo
import time
from Traj3D import Traj3D
from RotTable import RotTable
from table import Table
from evaluation import Evaluation

# ========== # VARIABLES MODIFIABLE POUR FAIRE DES TESTS # ========== #

Nb_explo = 10  # Choix du nombre de sommet à explorer
filename = "MonteCarlo\plasmid_8k.fasta"  # Choix du fichier de sequence

# ========== # CREATION DE seq ET APPEL DE LA CLASSE # ========== #

traj = Traj3D()
lineList = [line.rstrip('\n') for line in open(filename)]
seq = ''.join(lineList[1:])

MCTS = MonteCarlo(Table.get_original(), Table, Evaluation, seq, Nb_explo)

# ========== # INITIALISATION DES VARIABLES POUR LES TESTS CI DESSOUS # ========== #

# On prend le tree initial qui contient que la racine
#tree = MCTS.tree

# On crée une nouvelle gen depuis la racine
# MCTS.gen(tree)
# children1 = tree['children']


# # On crée une nouvelle gen depuis l'enfant numero 0 de la racine
# new_gen2 = Table(children1['t0'])

# ========== # TEST DE LA PROFONDEUR # ========== #

# print(new_gen2.get_depth())

# ========== # TEST DU RANDOM GEN # ========== #

# sommet_random = new_gen2.gen_random()
# print(sommet_random, '\n \n')

# ========== # TEST DE LA MODIFICATION DU COEFF + CREATION DES SOMMETS ENFANTS # ========== #

# for sommet in children1:
#     print(sommet+'\n', children1[sommet], '\n')

# ========== # TEST DE LA 2EME GEN # ========== #

# children2 = new_gen2.children()
# for sommet in children2:
#     print(sommet+'\n', children2[sommet]['table'], '\n')
# print(len(new_gen.children()))

# ========== # TEST DE L'EVALUATION # ========== #

# MCTS.gen(tree)
# bestNode = MCTS.selection()
# print('Le best Node avant évaluation est : \n', bestNode, '\n \n')
# print('Le score de bestNode est : \n', bestNode['score'], '\n \n')

# MCTS.eval_and_update_score(bestNode)
#print('Le best Node après évaluation est : \n', bestNode, '\n \n')

# print(tree)
# bestNode = MCTS.selection()
# MCTS.eval_and_update_score(bestNode)
# print('Le best Node après évaluation est : \n', bestNode, '\n \n')

# print('Si on regarde les score des bestNode["parent"]["children"]')
# for enfant in bestNode['parent']['children']:
#     print(bestNode['parent']['children'][enfant]['score'])

# print('\n Si on regarde les score des tree["children"]')
# for enfant in tree['children']:
#     print(tree['children'][enfant]['score'])

# print("\n \nL'arbre final est: \n", tree)


# ========== # TEST FINAL # ========== #

start_time = time.time()

bestNode = MCTS.process()
best_table = bestNode['table']

print("\n\n--- MonteCarlo a pris %s seconds ---" % (time.time() - start_time))
print("\n \nLa BestRotTable est : \n", best_table, "\n \n")
print("Son score selon son sommet est :", bestNode['score'], '\n \n')
print("Son score selon Evaluation est :",
      Evaluation(seq, best_table).result, '\n \n')

best_rot_table = RotTable()
best_rot_table.writeRotTable(best_table)
traj.compute(seq, best_rot_table)
traj.draw("plasmid_8k.fasta"+".png")
