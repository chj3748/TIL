# 최단거리 다익스트라 그래프 | bj 1753 최단경로

# import sys
# def dijkstra(K, V, graph):
#     INF = sys.maxsize
#     s = [0] * V
#     d = [INF] * V
#     d[K - 1] = 0
#     while True:
#         m = INF
#         N = -1
#
#         for j in range(V):
#             if not s[j] and m > d[j]:
#                 m = d[j]
#                 N = j
#
#         if m == INF:
#             break
#
#         s[N] = 1
#         for j, weight in graph[N]:
#             if s[j]: continue
#             via = d[N] + weight
#             if d[j] > via:
#                 d[j] = via
#         # for j in range(V):
#         #     if s[j]: continue
#         #     via = d[N] + graph[N][j]
#         #     if d[j] > via:
#         #         d[j] = via
#     return d
#
#
# V, E = map(int, input().split())
# K = int(input())
# INF = sys.maxsize
# graph = {i: [] for i in range(V)}
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     # graph[u - 1][v - 1] = w
#     graph[u - 1].append((v - 1, w))
#     # graph[v-1].append([u-1, w])
#
# for d in dijkstra(K, V, graph):
#     print(d if d != INF else "INF")

## 속도 개선 및 힙큐 사용 다익스트라
import sys

# import itertools
# from math import factorial
# from collections import deque
import heapq

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

V, E = map(int, inp().split())
start = int(inp())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    # 출발점, 도착점, 가중치
    u, v, w = map(int, inp().split())
    graph[u].append([v, w])

inf = int(1e9)


def dijkstra(start):
    distance = [inf] * (V + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for neighbor, weight in graph[now]:
            if distance[neighbor] > distance[now] + weight:
                distance[neighbor] = distance[now] + weight
                heapq.heappush(q, (distance[neighbor], neighbor))
    return distance


answer = dijkstra(start)

for i in range(1, V + 1):
    print(answer[i] if answer[i] != inf else 'INF')

