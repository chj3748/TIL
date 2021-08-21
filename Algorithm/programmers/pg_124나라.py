# math | programmers 124나라
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()

# 쉬운듯 하면서도 어려운 문제라고 생각함
# 핵심은 삼진법처럼 생겼지만, 일반 진법과 다르게 0이 없기때문에 n - 1로 고려하는것
def solution(n):
    answer = []
    while n > 0:
        n, mod = divmod(n - 1, 3)
        answer.append(1 if mod == 0 else (2 if mod == 1 else 4))
    return ''.join(map(str, answer[::-1]))