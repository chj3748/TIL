import heapq

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    ajd = {i: [] for i in range(V + 1)}
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        ajd[n1].append([n2, w])
        ajd[n2].append([n1, w])
    INF = float('inf')
    mst = [False] * (V + 1)
    key = [INF] * (V + 1)
    key[0] = 0
    hq = []
    heapq.heappush(hq, (0, 0))
    result = 0
    while hq:
        k, node = heapq.heappop(hq)
        if mst[node]:
            continue
        result += k
        mst[node] = True
        for next_node, we in ajd[node]:
            if not mst[next_node] and key[next_node] > we:
                key[next_node] = we
                heapq.heappush(hq, (we, next_node))
    print('#{} {}'.format(t, result))
