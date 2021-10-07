# deque pq | programmers 프린터
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(priorities, location):
    from collections import deque
    checked = sorted(priorities)
    p = deque([[idx, val] for idx, val in enumerate(priorities)])
    cnt = 0
    while deque:
        if p[0][1] == checked[-1]:
            cnt += 1
            checked.pop()
            temp = p.popleft()
            if temp[0] == location:
                break
        else:
            p.rotate(-1)
    return cnt