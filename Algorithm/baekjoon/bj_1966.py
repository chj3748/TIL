# dp | bj 1966 프린터 큐
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

for t in range(int(input())):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    deq = deque()
    for i in range(N):
        deq.append([priority[i], i])

    orders = [0] * N
    priority.sort()
    order = 1
    while not orders[M]:
        if deq[0][0] >= priority[-1]:
            pr, work = deq.popleft()
            priority.pop()
            orders[work] = order
            order += 1
        else:
            deq.rotate(-1)
    else:
        print(orders[M])
