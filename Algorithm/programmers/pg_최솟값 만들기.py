# sort math | programmers 최솟값 만들기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])
