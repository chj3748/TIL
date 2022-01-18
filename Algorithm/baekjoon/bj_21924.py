# mst | baekjoon 21924 도시 건설
# github.com/chj3748
import sys
import heapq
sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().rstrip()


total_cost = 0
N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
roads = []
for _ in range(M):
    b1, b2, cost = map(int, input().split())
    total_cost += cost
    heapq.heappush(roads, [cost, b1, b2])


def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union(x1, x2):
    x1_p, x2_p = parents[x1], parents[x2]
    if x1_p <= x2_p:
        parents[x2_p] = x1_p
    else:
        parents[x1_p] = x2_p


cnt_road = 0
build_cost = 0
while roads and cnt_road != N - 1:
    cost, b1, b2 = heapq.heappop(roads)
    b1_p, b2_p = find_parent(b1), find_parent(b2)
    if b1_p == b2_p:
        continue
    union(b1, b2)
    cnt_road += 1
    build_cost += cost

print(total_cost - build_cost if cnt_road == N - 1 else -1)