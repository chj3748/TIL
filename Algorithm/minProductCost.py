# swea 5209 최소 생산 비용
def choice(idx,N,cost):
    global min_cost
    if cost >= min_cost:
        return
    if idx == N :
        min_cost = min(min_cost, cost)
        return
    for i in range(N):
        if used[i] == 1:
            continue
        used[i]=1
        choice(idx+1, N, cost+factories[idx][i])
        used[i]=0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    factories = [ list(map(int,input().split())) for _ in range(N) ]

    global min_cost
    min_cost = 15*99

    used = [0] *N

    choice(0,N,0)

    print('#{} {}'.format(t, min_cost))