# swea dijkstra graph | 5251 최소이동거리
T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V + 1)}
    for _ in range(E):
        start, end, w = map(int, input().split())
        adj[start].append((end, w))
    INF = float('inf')
    distance_list = [INF] * (V + 1)
    mst = [True] * (V + 1)
    distance_list[0] = 0
    node = 0
    result = 0
    while node != V:
        mst[node] = False
        for next_node, distance in adj[node]:
            distance_list[next_node] = min(distance_list[next_node], distance_list[node] + distance)
        next_min_distance = INF
        next_min_node = -1
        for ind in range(V + 1):
            if mst[ind] and next_min_distance > distance_list[ind]:
                next_min_distance = distance_list[ind]
                next_min_node = ind
        node = next_min_node
    print('#{} {}'.format(t, distance_list[V]))
