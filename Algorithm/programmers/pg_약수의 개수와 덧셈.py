# math | programmers 약수의 개수와 덧셈
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(left, right):
    return sum([-i if i ** (1 / 2) % 1 == 0 else i for i in range(left, right + 1)])
