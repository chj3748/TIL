# unionfind mst 크루스칼 프림 | bj 4386 별자리 만들기
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

stars = [list(map(float, input().split())) for _ in range(n)]
parents = [i for i in range(n + 1)]
edges = []
def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parents(a, b):
    a_parent = find_parent(a)
    b_parent = find_parent(b)
    if a_parent < b_parent:
        parents[b_parent] = a_parent
    else:
        parents[a_parent] = b_parent

for i in range(n - 1):
    for j in range(i + 1, n):
        star1 = stars[i]
        star2 = stars[j]
        cost = ((star1[0] - star2[0])**2 + (star1[1] - star2[1])**2)**(1/2)
        heapq.heappush(edges, [cost, i + 1, j + 1])

cnt = 0
total_cost = 0
while cnt < n - 1:
    cost, s1, s2 = heapq.heappop(edges)
    if find_parent(s1) != find_parent(s2):
        union_parents(s1, s2)
        total_cost += cost
        cnt += 1

print(f'{total_cost:.2f}')