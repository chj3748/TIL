# hash | programmers 위장
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(clothes):
    from collections import defaultdict
    types = defaultdict(int)
    for cloth in clothes:
        types[cloth[1]] += 1
    answer = 1
    for key, val in types.items():
        answer *= (val + 1)
    return answer - 1
