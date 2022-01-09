# 누적합 | codility TapeEquilibrium
# github.com/chj3748
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def solution(A):
    for i in range(1, len(A)):
        A[i] += A[i - 1]

    min_val = int(1e9)
    for i in range(len(A) - 1):
        temp = abs(A[i] - (A[-1] - A[i]))
        if min_val > temp:
            min_val = temp
    return min_val