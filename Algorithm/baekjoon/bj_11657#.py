# 최단거리 벨만포드 그래프 | bj 11657 타임머신
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N, M = map(int, inp().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s_city, d_city, time = map(int, inp().split())
    graph[s_city].append([d_city, time])

q = []

# 벨만 포드 알고리즘은 다익스트라 알고리즘이 가중치가 양의 정수일때만 가능한것에 대해
# 음의 가중치를 가질때도 해결 가능한 알고리즘이다
# 단, 음의 가중치를 갖는 특성상 최단거리가 음의 무한대로 가는 싸이클이 존재 할 수 있다.
# 음의 싸이클을 막기위해서는 선택해야하는 최소 간선의 수만 큼을 선택하면 된다(N -1)
# 음의 싸이클이 존재하는지 확인하기 위해서는 N번째 간선을 선택하는 과정을 통해서 최단거리가 수정된다면 음의 싸이클이 존재한다는 것
def bellman_ford(start):
    distance = [int(1e9)] * (N + 1)
    distance[0] = distance[start] = 0
    for _ in range(1, N):  # 정점 개수 - 1, 즉 선택해야하는 간선개수인 N -1만큼 실행
        for node in range(1, N + 1):
            for neighbor, n_time in graph[node]:
                # node의 거리값이 수정된적 없다는것은 아직 갈수 없다는것인데
                # 갈 수 없는 곳의 거리비교는 무의미함
                if distance[node] == int(1e9):
                    continue
                # node에서 neighbor까지 가는데 지금까지의 최단거리와 새로운 경로의 거리를 비교
                if distance[neighbor] > distance[node] + n_time:
                    distance[neighbor] = distance[node] + n_time

    for node in range(1, N + 1):
        for neighbor, n_time in graph[node]:
            if distance[node] == int(1e9):
                continue
            if distance[neighbor] > distance[node] + n_time:
                return None

    return distance


answer = bellman_ford(1)
if answer is None:
    print(-1)
else:
    for ans in answer[2:]:  # 출발점이 1도시로 고정이니 2도시부터 최단거리 출력
        print(ans if ans != int(1e9) else -1)  # 만약 갈수없으면(한번도 수정된적 없으면) -1 출력
