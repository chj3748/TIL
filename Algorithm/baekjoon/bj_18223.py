# 그래프 다익스트라 | bj 18223 민준이와 마산 그리고 건우
# github.com/chj3748
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


V, E, P = map(int, input().split())
edges = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, c = map(int, input().split())
    edges[s].append([c, e])
    edges[e].append([c, s])

inf = float('inf')
start_1 = [inf] * (V + 1)
start_p = [inf] * (V + 1)


def djikstra_1():
    start_1[1] = 0
    hq = []
    heapq.heappush(hq, (0, 1))
    while hq:
        dist, curr = heapq.heappop(hq)
        if start_1[curr] < dist:
            continue
        for c, e_idx in edges[curr]:
            cost = dist + c
            if start_1[e_idx] > cost:
                start_1[e_idx] = cost
                heapq.heappush(hq, (cost, e_idx))


def djikstra_p(start):
    start_p[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        dist, curr = heapq.heappop(hq)
        if start_p[curr] < dist:
            continue
        for c, e_idx in edges[curr]:
            cost = dist + c
            if start_p[e_idx] > cost:
                start_p[e_idx] = cost
                heapq.heappush(hq, (cost, e_idx))


djikstra_1()
djikstra_p(P)
if start_1[V] >= start_1[P] + start_p[V]:
    print('SAVE HIM')
else:
    print('GOOD BYE')
