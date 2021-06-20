# mst | bj 16398 행성 연결
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
all_costs = [list(map(int, input().split())) for _ in range(N)]
costs = []
for i in range(N - 1):
    for j in range(i + 1, N):
        heapq.heappush(costs, [all_costs[i][j], i, j])
parents = [i for i in range(N)]

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union(x1, x2):
    if x1< x2:
        parents[x2] = x1
    else:
        parents[x1] = x2

cnt = 0
answer = 0
while cnt != N - 1:
    cost, p1, p2 = heapq.heappop(costs)
    p1_p = find_parent(p1)
    p2_p = find_parent(p2)
    if p1_p != p2_p:
        union(p1_p, p2_p)
        cnt += 1
        answer += cost

print(answer)

