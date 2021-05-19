# 다익스트라 그래프 | bj 11779 최소비용 구하기 2
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
m = int(input())
inf = float('inf')
# 버스 노선 처리
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

# 도시별 도착 최소 비용
min_cost = [inf] * (n + 1)
# 출발점, 도착점
s, e = map(int, input().split())

## 여기서 부터 다익
min_cost[s] = 0
h = []
heapq.heappush(h, (0, s, [s]))
route = []
while h:
    payed, node, visited = heapq.heappop(h)
    if min_cost[node] < payed:
        continue
    for next_city, bus_cost in graph[node]:
        next_cost = payed + bus_cost
        if next_cost < min_cost[next_city]:
            if next_city == e:
                route = visited + [next_city]
            min_cost[next_city] = next_cost
            heapq.heappush(h, (next_cost, next_city, visited + [next_city]))

print(min_cost[e])
print(len(route))
print(*route)
