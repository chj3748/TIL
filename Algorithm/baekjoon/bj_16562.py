# union-find | bj 16562 친구비
# github.com/chj3748
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]


def union(x1, x2):
    parent_x1 = find_parents(x1)
    parent_x2 = find_parents(x2)
    if parent_x1 < parent_x2:
        parents[parent_x2] = parent_x1
    else:
        parents[parent_x1] = parent_x2


N, M, k = map(int, input().split())
hq = []
for idx, cost in enumerate(map(int, input().split())):
    heapq.heappush(hq, [cost, idx + 1])

parents = [i for i in range(N + 1)]

for _ in range(M):
    f1, f2 = map(int, input().split())
    union(f1, f2)

total_cost = 0
while hq:
    c, i = heapq.heappop(hq)
    parent_i = find_parents(i)
    if parent_i != 0:
        union(0, i)
        total_cost += c
else:
    if total_cost > k:
        answer = 'Oh no'
    else:
        answer = total_cost
print(answer)