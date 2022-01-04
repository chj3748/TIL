# greedy | codility MaxCounters
# github.com/chj3748
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def solution(N, A):
    cnt = defaultdict(int)
    mc = 0
    m = 0
    for v in A:
        if v == N + 1:
            cnt = defaultdict(int)
            mc = m
            continue
        cnt[v - 1] += 1
        if m < cnt[v - 1] + mc:
            m = cnt[v - 1] + mc

    answer = [mc] * N
    for k, v in cnt.items():
        answer[k] += v
    return answer