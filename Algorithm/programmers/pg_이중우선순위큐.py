# 우선순위큐 heap | programmers 이중우선순위큐
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


from collections import defaultdict
import heapq

used = defaultdict(int)
minheap = []
maxheap = []


def is_in(t):
    while minheap if t == -1 else maxheap:
        check = -heapq.heappop(maxheap) if t == 1 else heapq.heappop(minheap)
        if used[check] < 1:
            continue
        else:
            used[check] -= 1
            break
    else:
        return 0
    return check


def solution(operations):
    for operation in operations:
        cmd, num = operation.split()
        num = int(num)
        if cmd == 'I':
            used[num] += 1
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
        else:
            is_in(num)

    if maxheap and minheap:
        maxnum = is_in(1)
        minnum = is_in(-1)
        answer = [maxnum, minnum]
    else:
        answer = [0, 0]
    return answer