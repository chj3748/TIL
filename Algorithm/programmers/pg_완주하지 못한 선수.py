# hash | programmers 완주하지 못한 선수
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(participant, completion):
    sorted_p = sorted(participant)
    sorted_c = sorted(completion)
    for i in range(len(sorted_c)):
        if sorted_p[i] != sorted_c[i]:
            return sorted_p[i]
    return sorted_p[-1]