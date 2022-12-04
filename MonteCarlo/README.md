# Monte Carlo Tree Search (MCTS)

# Principe de l’algorithme 

L’algorithme de Monte Carlo est un algorithme d’optimisation qui permet, depuis une configuration initiale, de créer les configurations suivantes ainsi que de les évaluer. Il va ensuite effectuer un parcours de graphe afin de chercher les solutions les plus prometteuses et en générer les configurations suivantes. 

L’algorithme de parcours de graphe de Monte Carlo se base initialement sur le ratio de partie réussie / partie simulée, ici, l’indicateur permettant d’évaluer quel sommet est le meilleur sera la distance entre les deux extrémités de la chaîne de nucléotides.  

# Fonctionnement détaillé  

## Initialisation 

L’algorithme MCTS crée la racine du graphe à l’aide de la configuration initiale qui lui est donnée. La structure adoptée ici pour un sommet est la suivante :  

node = {‘table’: rot_table, ‘children’:{‘node1’:{..}, ’node2’:{..},..}, ‘parent’: parent_node, ‘score’: score } 

L’étape suivante est la création de la première génération de fils : Fonction gen()  

Puis l’évaluation de tous les fils : Fonction eval_and_update() 

## Récursivité 

On procède à la sélection : On part de la racine et on descend en profondeur dans l’arbre en choisissant le nœud avec le score le plus faible à chaque étage : Fonction selection() 

Une fois arrivé à la profondeur de nœuds terminaux : 

S'il y a un nœud terminal non évalué, on l’évalue (même évaluation que pour l’algo gen) 

S'ils sont tous évalués, on choisit celui avec le score le plus faible 

On procède à la génération depuis ce nœud 

On évalue un nœud de cette nouvelle génération et on met à jour son score ainsi que celui de tous ses ascendants. Pour évaluer les nœuds : 

Pour le nœud terminal on fait N simulations (N étant une entrée pour MCTS) aléatoires en faisant varier les coefficients encore non fixés, on en prend ensuite la moyenne. 

Pour un nœud qui a des enfants, on fait la moyenne des scores des enfants évalués. 

On reprend le procédé. 

 

# Structure du code 

On a donc dans MCTS les fonctions : 

gen() 

Eval_and_update() 

Selection() 

Process() (fonction qui exécute tout l’algorithme et renvoie le meilleur sommet trouvé) 

 
Puisque cet algorithme est entièrement générique, il lui est nécessaire de faire appel à une autre classe qui agira sur les objets traités dans les sommets (ici ce sont des rot_table sous forme de dictionnaire mais cela aurait pu être une matrice par exemple).  En l’occurrence, on utilisera la classe Table. Cette dernière dispose des méthodes suivantes : 

Get_depth() : permet de connaitre la profondeur dans l’arbre d’un sommet 

Children() : crée une table fils en fonction de la profondeur de la table (Modifie seulement les coefficients encore non traités) 

Gen_random() : génère une table aléatoire sans modifier les coefficients déjà choisis. 

# Comment lancer le code ?

Ouvrir le fichier simulation.py, il y a en haut du code une section de variables à modifier qui comprend la modification du nom du fichier ainsi que du nombre de sommet à explorer par l'algo. Une fois ces deux paramètres rempli, on peut excuter le fichier. On obtient en sortie le tracé, le score du noeud dans le graphe, le score réel du noeud (celui de la table), et la table. 