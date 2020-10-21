# swea dp djikstra | 1251 하나로
T = int(input())
for t in range(1, T + 1):
    INF = float('inf')
    N = int(input())
    islands = {i: [] for i in range(N)}
    idx = 0
    for y in map(int, input().split()):
        islands[idx].append(y)
        idx += 1
    idx = 0
    for x in map(int, input().split()):
        islands[idx].append(x)
        idx += 1
    E = float(input())
    distance_list = [INF] * N
    checked = [0] * N
    distance_list[0] = 0
    node = 0
    cnt = N
    while cnt != 0:
        checked[node] = 1
        for next_node in range(N):
            if checked[next_node] == 0:
                distance = (islands[node][0] - islands[next_node][0]) ** 2 + (islands[node][1] - islands[next_node][1]) ** 2
                distance_list[next_node] = min(distance_list[next_node], distance)
        next_min_distance = INF
        next_min_node = -1
        cnt -= 1
        for idx in range(N):
            if checked[idx] == 0 and next_min_distance > distance_list[idx]:
                next_min_distance = distance_list[idx]
                next_min_node = idx
        node = next_min_node
    result = sum(distance_list)
    print('#{} {}'.format(t, round(E * result)))
