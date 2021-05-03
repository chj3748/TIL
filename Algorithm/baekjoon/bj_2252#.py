# 위상정렬 그래프 | bj 2252 줄세우기
import sys

# import itertools
# from math import factorial
from collections import deque

# import heapq

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N, M = map(int, inp().split())
indegree = [0] * (N + 1)  # 진입차수를 기록할 리스트
graph = [[] for _ in range(N + 1)]  # 간선정보를 저정할 리스트
for _ in range(M):
    smaller, taller = map(int, inp().split())
    indegree[taller] += 1
    graph[smaller].append(taller)

q = deque()
answer = []

for i in range(1, N + 1):  # 진입차수가 0인
    if indegree[i] == 0:   # 즉 자기보다 키가 작은 사람이 없는 학생들을 모조리 큐에 넣음
        q.append(i)

while q:
    someone = q.popleft()
    answer.append(someone)
    for next_one in graph[someone]:      # 누군가의 다음 학생 중
        if indegree[next_one] > 0:
            indegree[next_one] -= 1      # 현재 학생(누군가)을 제외하면
            if indegree[next_one] == 0:  # 자기보다 키가 작은 학생이 없다면
                q.append(next_one)       # 큐에 넣음

print(' '.join(map(str, answer)))
