# 순열 | baekjoon 15649 N과 M(1)
# github.com/chj3748
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
used = defaultdict(int)


def make_permu(k, answer):
    if k == M:
        print(' '.join(map(str, answer)))
        return
    for num in range(1, N + 1):
        if used[num]:
            continue
        used[num] = 1
        make_permu(k + 1, answer + [num])
        used[num] = 0


make_permu(0, [])
