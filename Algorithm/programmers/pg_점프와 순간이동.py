# 이진법 math | programmers 점프와 순간이동
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n):
    answer = 0
    for one in bin(n):
        if one == '1':
            answer += 1
    return answer