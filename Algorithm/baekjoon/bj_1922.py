# unionfind 서로소집합 mst 크루스칼 그래프 | bj 1922 네트워크 연결
import sys

# import itertools
# from math import factorial
# from collections import deque
import heapq

sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N, M = int(inp()), int(inp())
computers = [[] for _ in range(N + 1)]
h = []
# 비용이 저렴한것부터 오름차순으로 뽑을것이기 때문에 힙큐써버림
for _ in range(M):
    com1, com2, cost = map(int, inp().split())
    heapq.heappush(h, [cost, com1, com2])

parents = [i for i in range(N + 1)]  # 각 컴퓨터의 최상위 컴퓨터 기록


def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)
    if a_parent < b_parent:
        parents[b_parent] = a_parent
    elif a_parent > b_parent:
        parents[a_parent] = b_parent


answer = 0
while h:
    cost, com1, com2 = heapq.heappop(h)
    if find_parent(com1) != find_parent(com2):  # 두 컴퓨터의 부모가 다르다
        answer += cost                          # 즉 연결되어있지 않다면 비용 추가하고 연결
        union_parent(com1, com2)

print(answer)
