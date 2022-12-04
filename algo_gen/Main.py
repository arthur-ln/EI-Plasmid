from Traj3D import Traj3D
from algo_gen import Algo_gen

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--filename", help="input filename of DNA sequence")
parser.add_argument("--N", help="population length")
parser.add_argument("--T", help="cycle number")

parser.parse_args()
args = parser.parse_args()


def main():
    N = int(args.N)
    T = int(args.T)
    traj = Traj3D()

    # Read file
    lineList = [line.rstrip('\n') for line in open(args.filename)]
    # Formatting
    seq = ''.join(lineList[1:])

    traj = Traj3D()
    algo = Algo_gen(seq, N, T)
    algo.boucle__gen()

    best_individu = algo.best_individu
    best_score = algo.best_result
    worst_score = algo.worst_result
    best_distance = algo.best_distance
    indice_max = algo.indice_max
    indice_min = algo.indice_min
    pop_score = algo.pop_score

    print(f'N={N}', f'T={T}', f'score={best_score}', f'worst={worst_score}',
          f'distance={best_distance}', f'indice_min={indice_min}', f'indice_max={indice_max}')
    print(pop_score)

    best_Rot_table = best_individu.Rot_table

    traj.compute(seq, best_Rot_table)

    traj.draw(args.filename+".png")


if __name__ == "__main__":
    main()
