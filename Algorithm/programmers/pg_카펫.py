# 완전탐색 | programmers 카펫
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, int((total ** 0.5) + 1)):
        x, y = i, total // i
        if total % i:
            continue
        if brown == x * 2 + (y - 2) * 2:
            return [y, x]