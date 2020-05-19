# swea 5189 전자카트
def b_f(start, goal, total, k, visited):
    global min_battery
    if goal == 0 :
        min_battery = min(min_battery, total)
        return
    if k == N-1:
        b_f(goal, 0, total+golf[start][0], k+1, visited)
    else:
        for idx, next in enumerate(golf[start]):
            if idx not in visited:
                b_f(idx, goal, total+next, k+1, visited+[idx])



for t in range(1,int(input())+1):
    N = int(input())
    golf = [ list(map(int,input().split())) for _ in range(N) ]

    global min_battery
    min_battery=1000

    b_f(0,N,0,0,[0])

    print('#{} {}'.format(t, min_battery))