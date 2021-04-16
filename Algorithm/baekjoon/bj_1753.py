# graph mst dijkstra | 1753 최단 경로
import sys


def dijkstra(K, V, graph):
    INF = sys.maxsize
    s = [0] * V
    d = [INF] * V
    d[K - 1] = 0
    while True:
        m = INF
        N = -1

        for j in range(V):
            if not s[j] and m > d[j]:
                m = d[j]
                N = j

        if m == INF:
            break

        s[N] = 1
        for j, weight in graph[N]:
            if s[j]: continue
            via = d[N] + weight
            if d[j] > via:
                d[j] = via
        # for j in range(V):
        #     if s[j]: continue
        #     via = d[N] + graph[N][j]
        #     if d[j] > via:
        #         d[j] = via
    return d


V, E = map(int, input().split())
K = int(input())
INF = sys.maxsize
graph = {i: [] for i in range(V)}
for _ in range(E):
    u, v, w = map(int, input().split())
    # graph[u - 1][v - 1] = w
    graph[u - 1].append((v - 1, w))
    # graph[v-1].append([u-1, w])

for d in dijkstra(K, V, graph):
    print(d if d != INF else "INF")
