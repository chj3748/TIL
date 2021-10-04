# math | programmers 숫자의 표현
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n):
    cnt = 1
    for i in range(n // 2 + 1, 3, -1):
        temp = i
        for j in range(i - 1, 0, -1):
            if temp >= n:
                break
            temp += j
        if temp == n:
            cnt += 1
    return cnt
