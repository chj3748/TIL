# swea bfs | 5521 상원이의 생일파티
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    friends = {i: [] for i in range(N + 1)}
    for _ in range(M):
        f1, f2 = map(int, input().split())
        friends[f1].append(f2)
        friends[f2].append(f1)
    friends[0] = list(friends[1])
    for f in friends[1]:
        for ff in friends[f]:
            if ff != 1 and ff not in friends[0]:
                friends[0].append(ff)
    print('#{} {}'.format(t, len(friends[0])))
