# mst | bj 1414 불우이웃돕기
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
length = {}
for i in range(26):
    length[chr(ord('a') + i)] = i + 1
for i in range(26):
    length[chr(ord('A') + i)] = i + 27

rooms = [list(input()) for _ in range(N)]
costs = []
total = 0
for i in range(N):
    for j in range(N):
        if rooms[i][j] == '0':
            continue
        heapq.heappush(costs, [length[rooms[i][j]], i, j])
        total += length[rooms[i][j]]
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
while costs:
    cost, p1, p2 = heapq.heappop(costs)
    p1_p = find_parent(p1)
    p2_p = find_parent(p2)
    if p1_p != p2_p:
        union(p1_p, p2_p)
        cnt += 1
        answer += cost

if cnt == N - 1:
    result = total - answer
else:
    result = -1
print(result)