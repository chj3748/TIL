# swea dp 완전탐색? bfs | 1249 보급로
def find_route(s, g):
    q = [start]
    while q:
        y, x = q.pop(0)
        for d in (0, 1), (1, 0), (-1, 0), (0, -1):
            ny, nx = y + d[0], x + d[1]
            if 0 <= ny < N and 0 <= nx < N:
                next_cost = route_cost[y][x] + road[ny][nx]
                if next_cost < route_cost[ny][nx]:
                    q.append((ny, nx))
                    route_cost[ny][nx] = next_cost


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]
    start, goal = (0, 0), (N - 1, N - 1)
    route_cost = [[float('inf')] * N for _ in range(N)]
    route_cost[0][0] = 0
    find_route(start, goal)
    print('#{} {}'.format(t, route_cost[N - 1][N - 1]))