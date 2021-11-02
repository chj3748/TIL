# 투포인터 greedy | programmers 구명보트
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(people, limit):
    from collections import deque
    dq = deque(sorted(people))
    answer = 0
    while dq:
        answer += 1
        big_people = dq.pop()
        if not dq:
            continue
        if dq[0] + big_people <= limit:
            dq.popleft()
    return answer