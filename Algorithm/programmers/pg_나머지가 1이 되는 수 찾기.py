# math | programmers 나머지가 1이 되는 수 찾기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n):
    for i in range(1, 1000000):
        if n % i == 1:
            return i