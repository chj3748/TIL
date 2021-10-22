# 재귀 math | programmers 모음사전
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(word):
    answer = 0
    def my_product(idx, val):
        nonlocal answer
        if val == word:
            return True
        if idx > 5:
            return False
        answer += 1
        for d in ['A', 'E', 'I', 'O', 'U']:
            temp = my_product(idx + 1, val + d)
            if temp:
                return True
    my_product(0, '')
    return answer