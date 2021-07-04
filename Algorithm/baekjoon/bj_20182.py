# 다익스트라 우선순위큐 | bj 20182 골목 대장 호석 - 효율성 1
# github.com/chj3748
# 이분 탐색으로 다른 접근도 가능, 금액이 0~20밖에 안되기때문에 금액기준으로 하면 더빠르다

import sys
import heapq
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()


N, M, A, B, C = map(int, input().split())
paths = defaultdict(list)
for _ in range(M):
    s, e, cost = map(int, input().split())
    paths[s].append([cost, e])
    paths[e].append([cost, s])

inf = float('inf')
costs = [[inf, inf]] * (N + 1)  # [total, max]
costs[A] = [0, 0]

pq = []
heapq.heappush(pq, [0, A])
while pq:
    cost, node = heapq.heappop(pq)
    if node == B:
        break
    for next_cost, next_node in paths[node]:
        temp = costs[node][0] + next_cost
        before_max = max(costs[node][1], next_cost)
        if temp <= C:
            if costs[next_node][1] > before_max:
                costs[next_node] = [temp, before_max]
                heapq.heappush(pq, [next_cost, next_node])

print(costs[B][1] if costs[B][1] != inf else -1)
