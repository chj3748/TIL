# mst unionfind | bj 2887 행성 터널
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


def find_parent(p):
    if p_parents[p] != p:
        p_parents[p] = find_parent(p_parents[p])
    return p_parents[p]


def union_planet(p1, p2):
    p1_parent = find_parent(p1)
    p2_parent = find_parent(p2)
    if p1_parent == p2_parent:
        return False
    if p1_parent < p2_parent:
        p_parents[p2_parent] = p1_parent
    else:
        p_parents[p1_parent] = p2_parent
    return True


N = int(input())
planets = []
p_parents = [i for i in range(N)]
edges = []

for i in range(N):
    p_info = list(map(int, input().split()))
    planets.append(p_info+[i])
    # 행성과의 모든 연결 고리
    # for j in range(0, i):
    #     p1x, p1y, p1z = planets[i]
    #     p2x, p2y, p2z = planets[j]
    #     cost = min(abs(p1x - p2x), abs(p1y - p2y), abs(p1z - p2z))
    #     heapq.heappush(edges, [cost, i, j])

# 각각의 기준으로 정렬 후 좌우 인접한 행성끼리 연결한 경우
# x정렬, y정렬, z정렬
for sort_n in range(3):
    planets.sort(key=lambda x: x[sort_n])
    for i in range(N - 1):
        p1x, p1 = planets[i][sort_n], planets[i][3]
        p2x, p2 = planets[i + 1][sort_n], planets[i + 1][3]
        heapq.heappush(edges, [abs(p1x - p2x), p1, p2])
answer = 0
cnt = 0  # 사용한 간선 개수
while edges:
    cost, p1, p2 = heapq.heappop(edges)
    if union_planet(p1, p2):
        answer += cost
        cnt += 1
        if cnt == N - 1:  # 최소한으로 연결했을때 n - 1개를 사용하면 사이클 없이 가능
            break
print(answer)
