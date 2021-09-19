# 그리디 | programmers 체육복
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, lost, reserve):
    answer = [1] * (n + 1)
    answer[0] = 0
    for l in lost:
        answer[l] -= 1
    for r in reserve:
        answer[r] += 1
    cnt = 0
    for i in range(1, n + 1):
        if answer[i] > 0:
            cnt += 1
        else:
            if answer[i - 1] == 2:
                answer[i - 1] -= 1
                answer[i] += 1
                cnt += 1
            elif i + 1 <= n and answer[i + 1] == 2:
                answer[i + 1] -= 1
                answer[i] += 1
                cnt += 1
    return cnt