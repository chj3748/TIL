# 누적합 | programmers 쿠키 구입
# github.com/chj3748
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def solution(cookie):
    answer = 0
    cookie = [0] + cookie
    n = len(cookie)
    for i in range(1, n):
        cookie[i] += cookie[i - 1]

    for s in range(n - 1):
        checked = defaultdict(int)
        for e in range(s + 1, n):
            temp = cookie[e] - cookie[s]
            if checked[temp / 2]:
                if temp / 2 > answer:
                    answer = temp / 2
            checked[temp] += 1
    return answer