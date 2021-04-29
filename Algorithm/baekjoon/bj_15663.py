# 백트래킹 | bj 15663 N과M
import sys
import itertools

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline


N, M = map(int, inp().split())
numbers = list(map(int, inp().split()))
numbers.sort()

permu = itertools.permutations(numbers, M)
permu = sorted(list(set(permu)))
for p in permu:
    print(' '.join(map(str, p)))
