# sort | programmers H-index
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(citations):
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:
            return i
    return len(citations)
