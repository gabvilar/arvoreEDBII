import random
import statistics
import time

from avl_tree import AVLTree
from rb_tree import RBTree

N = 10000 
REPETICOES = 10


def cenarios(n, seed=20250035487):  # seed fixa(minha matrícula) para não ter diferenças
    crescente = list(range(1, n + 1))
    aleatoria = crescente[:]
    random.Random(seed).shuffle(aleatoria)
    return {
        "Crescente": crescente,
        "Decrescente": crescente[::-1],
        "Aleatório": aleatoria,
    }


def executar(Tree, chaves):
    tempos = []
    for _ in range(REPETICOES):
        t = Tree()
        inicio = time.perf_counter()
        for k in chaves:
            t.insert(k)
        tempos.append((time.perf_counter() - inicio) * 1000)
    return t, statistics.median(tempos)


def main():
    print(f"{'cenário':<12} {'estrutura':<12} {'altura':<7} {'rotações':<9} tempo (ms)")
    for nome, chaves in cenarios(N).items():
        for Tree in (AVLTree, RBTree):
            t, ms = executar(Tree, chaves)
            print(f"{nome:<12} {t.name:<12} {t.height():<7} {t.rotations:<9} {ms:.1f}")
        print()


if __name__ == "__main__":
    main()