# math | programmers 다음 큰 숫자
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n):
    cnt = bin(n).count('1')
    for i in range(n + 1, 1000001):
        if cnt == bin(i).count('1'):
            return i