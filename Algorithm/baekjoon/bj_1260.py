# 그래프 dfs bfs | bj 1260 DFS와 BFS
import sys
from collections import defaultdict
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N, M, V = map(int, input().split())
visited = [0] * (N + 1)
edges = defaultdict(list)
for _ in range(M):
    s, e = map(int, input().split())
    edges[s].append(e)
    edges[e].append(s)

# 인접행렬를 쓰는 경우
# edges = [[0]*(N + 1) for _ in range(N + 1)]
# for _ in range(M):
#     s, e = map(int, input().split())
#     edges[s][e] = 1
#     edges[e][s] = 1
#
# def dfs(x):
#     route = []
#     stack = [x]
#     while stack:
#         x = stack.pop()
#         if visited[x] == 1:
#             continue
#         route.append(x)
#         visited[x] = 1
#         for i in range(N,0,-1):
#             if edges[x][i] == 1:
#                 if visited[i] == 0:
#                     stack.append(i)
#     print(*route)
#
# def bfs(x):
#     route = []
#     deq = deque([x])
#     while deq:
#         x = deq.popleft()
#         route.append(x)
#         for i in range(1, N + 1):
#             if edges[x][i] == 1:
#                 if visited[i] == 0:
#                     visited[i] = 1
#                     deq.append(i)
#     print(*route)

def dfs(x):
    route = []
    stack = [x]
    while stack:
        x = stack.pop()
        if visited[x] == 1:
            continue
        route.append(x)
        visited[x] = 1
        for n in edges[x][::-1]:
            if visited[n] == 0:
                stack.append(n)
    print(*route)



def bfs(x):
    route = []
    deq = deque([x])
    while deq:
        x = deq.popleft()
        route.append(x)
        for n in edges[x]:
            if visited[n] == 0:
                visited[n] = 1
                deq.append(n)
    print(*route)


for edge in edges.values():
    edge.sort()

dfs(V)
visited = [0] * (N + 1)
visited[V] = 1
bfs(V)
