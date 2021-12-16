# sort dp | programmers 최고의 집합
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, s):
    if n > s:
        return [-1]
    div, mod = divmod(s, n)
    answer = [div] * n
    for i in range(mod):
        answer[i] += 1
    return sorted(answer)