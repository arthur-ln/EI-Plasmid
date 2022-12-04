
Objectifs :

Il faut réussir, pour une chaîne quelconque de nucléotide, à faire évoluer les angles de la matrice de rotation à l’intérieur de leur intervalle d’incertitude (renseigné sur les 3 dernières colonnes) de sorte à ce que la chaîne face un rond. 

Il faut d’abord créer une fonction heuristique qui va évaluer si la représentation 3D d’une chaîne en fonction d’une certaine table de rotation est bonne, soit :
    Si les 2 bouts en extrémité de chaîne coincident 
    Si la chaine globale à une forme circulaire (avoir le moins de deviation brutale)

A partir de cette fonction d'évaluation d'une trajectoire 3d, on va :
    Créer l'algorithme de Monte Carlo : A partir de la racine qui correspond à la config initiale et qui a au début une valeur 0/0 (0 simulation réussie/0 simulations faites) de RotTable, on va créer une branche qui correspond à une nouvelle config, 
        

    Créer l'algo génétique
        On va générer une population initiale de matrice avec une certaine distrib puis on va les faire combattre en 1vs1. On garde ensuite les gagnants avec une certaine proba de prendre un perdant (pour avoir un max de diversité) mais il faut s'assurer de garder le meilleur si il se fait recaler injustement : c'est la SELECTION (Arthur). Ensuite on va faire se croiser les gagnants 2 à 2 en ... : c'est le CROISEMENT (Lucas). Puis vient la MUTATION (Ameur).
