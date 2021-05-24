# 그래프 dfs | bj 14267 회사 문화 1
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

parents = defaultdict(list)
number = 0
for val in list(map(int, input().split())):
    parents[val - 1].append(number)
    number += 1
praises = [0] * N

for _ in range(M):
    people, q = map(int, input().split())
    praises[people - 1] += q

for i in range(N):
    for j in parents[i]:
        praises[j] += praises[i]

print(*praises)


