# ST2 (Théorie des Jeux) - EI Algorithmique Génétique

# Principe de l’algorithme

L'algorithme est un algorithme génétique classique. On cherche à trouver l'individu qui minimise notre fonction évaluation. Pour cela on génère une population d'individus aléatoire, on sélectionne les meilleurs individus, on les croise, puis on fait des mutations et on refait un cycle etc...

# Structure du code

On a différents fichiers avec différentes classes

La classe qui génère les cycles de vie est algo_gen et regroupe les fonctions selection, croisement et mutation
La classe evaluation permet d'évaluer un individu
Les classes individus et population génèrent des individus et des populations



# Comment lancer le code ?

Afin de lancer le code, se placer dans le dosser algo_gen, taper dans le terminal :

python3 Main.py --filename 'plasmid_8k.fasta' --N 50 --T 100

On peut aussi utiliser le fichier plasmid_180k.fasta
N correspond au nombre d'individus dans une population
T correspond au nombre de cycles que l'on effectue

On récupère differentes informations en sortie sur le meilleur individu