# 누적합 | bj 2900 프로그램
# github.com/chj3748
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def something(k, v):
    idx = 0
    while idx < N:
        a[idx] += val
        idx += k


N, K = map(int, input().split())
a = [0] * N
k_n = defaultdict(int)
for jump_n in list(map(int, input().split())):
    k_n[jump_n] += 1
for key, val in k_n.items():
    something(key, val)
for i in range(1, N):
    a[i] += a[i - 1]
Q = int(input())
a = [0] + a
for _ in range(Q):
    s, e = map(int, input().split())
    print(a[e + 1] - a[s])
