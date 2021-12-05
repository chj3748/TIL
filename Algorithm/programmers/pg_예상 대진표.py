# math binary_search | programmers 예상 대진표
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n,a,b):
    answer = 0
    while a != b:
        a_div, a_mod = divmod(a, 2)
        a = a_div + a_mod
        b_div, b_mod = divmod(b, 2)
        b = b_div + b_mod
        answer += 1
    return answer