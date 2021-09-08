# 수학 | programmers 음양 더하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        sign = 1 if signs[i] else -1
        answer += sign * absolutes[i]
    return answer