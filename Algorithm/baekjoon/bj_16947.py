# dfs bfs 그래프 | bj 16947 서울 지하철 2호선
# 시간나면 다시 풀어보자
import sys
from collections import deque


sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
stations = [[] for _ in range(N + 1)]

for _ in range(N):
    s1, s2 = map(int, input().split())
    stations[s1].append(s2)
    stations[s2].append(s1)

d = [0] * (N + 1)
visited = [0] * (N + 1)

def dfs(x, cnt):
    # 이미 방문한 노드인데 거리차가 3 이상일 경우 사이클이 발생한다
    if visited[x]:
        if cnt - d[x] >= 3:
            return x
        else:
            return -1
    visited[x] = 1
    d[x] = cnt
    for y in stations[x]:
        cycleStartNode = dfs(y, cnt + 1)
        if cycleStartNode != -1:
            visited[x] = 2
            if x == cycleStartNode:
                return -1
            else:
                return cycleStartNode
    return -1
dfs(1, 0)

q = deque()
for i in range(1, N + 1):
    if visited[i] == 2:
        q.append(i)
        d[i] = 0
    else:
        d[i] = -1
while q:
    x = q.popleft()
    for y in stations[x]:
        if d[y] == -1:
            q.append(y)
            d[y] = d[x] + 1

print(*d[1:])