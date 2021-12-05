# math binary_search | programmers 예상 대진표
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, a, b):
    answer = 0
    while a != b:
        a = sum(divmod(a, 2))
        b = sum(divmod(b, 2))
        answer += 1
    return answer