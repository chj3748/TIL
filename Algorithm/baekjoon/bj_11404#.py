# 최단거리 플로이드워셜 그래프 | bj 11404 플로이드
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

n, m = int(inp()), int(inp())
inf = int(1e9)
graph = [[inf] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    # 출발도시, 도착도시, 비용
    a, b, c = map(int, inp().split())
    if graph[a][b] > c:
        graph[a][b] = c

# start도시에서 arrival도시까지 가는데 check도시를 경유해서 갈 경우의 최단거리
for check in range(1, n + 1):
    for start in range(1, n + 1):
        for arrival in range(1, n + 1):
            if graph[start][arrival] > graph[start][check] + graph[check][arrival]:
                graph[start][arrival] = graph[start][check] + graph[check][arrival]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == inf:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
