# mst kruskal | bj 14621 나만 안되는 연애
# github.com/chj3748
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
sex = input().split()
parents = [i for i in range(N)]
roads = []
for _ in range(M):
    u, v, d = map(int, input().split())
    if sex[u - 1] == sex[v - 1]:
        continue
    heapq.heappush(roads, [d, u - 1, v - 1])

def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union(x1, x2):
    x1_p = find_parent(x1)
    x2_p = find_parent(x2)
    if x1_p < x2_p:
        parents[x2_p] = x1_p
    else:
        parents[x1_p] = x2_p

cnt = 0
total_d = 0
while roads and cnt != N - 1:
    d, x1, x2 = heapq.heappop(roads)
    x1_p = find_parent(x1)
    x2_p = find_parent(x2)
    if x1_p == x2_p:
        continue
    union(x1, x2)
    cnt += 1
    total_d += d

if cnt != N - 1:
    print(-1)
else:
    print(total_d)