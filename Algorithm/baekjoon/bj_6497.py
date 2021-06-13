# mst | bj 6497 전력난
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


def find_parent(x):
    if h_parents[x] != x:
        h_parents[x] = find_parent(h_parents[x])
    return h_parents[x]


def union_parents(x, y):
    x_p = find_parent(x)
    y_p = find_parent(y)
    if x_p < y_p:
        h_parents[y_p] = x_p
    else:
        h_parents[x_p] = y_p


while True:
    m, n = map(int, input().split())
    if not m and not n:
        break
    loads = []
    total = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        heapq.heappush(loads, [z, x, y])
        total += z
    h_parents = [i for i in range(m)]

    answer = 0
    cnt = 0
    while cnt < m - 1:
        cost, h1, h2 = heapq.heappop(loads)
        h1p = find_parent(h1)
        h2p = find_parent(h2)
        if h1p != h2p:
            union_parents(h1, h2)
            cnt += 1
            answer += cost

    print(total - answer)
