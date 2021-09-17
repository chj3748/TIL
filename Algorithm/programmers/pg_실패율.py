# 누적합 | programmers 실패율
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(N, stages):
    before = [0] * (N + 2)
    after = [0] * (N + 2)
    for stage in stages:
        before[stage] += 1
    for i in range(1, N + 2):
        after[i] = after[i - 1] + before[i]
    return list(zip(*sorted([[0, i] if len(stages) - after[i - 1] == 0 else [before[i]/(len(stages) - after[i - 1]) ,i] for i in range(1, N + 1)], key = lambda x: [-x[0],x[1]])))[1]