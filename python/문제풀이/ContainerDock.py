# 5202 화물도크
for t in range(1, int(input()) + 1):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]
    time = list(sorted(time))

    result = []
    start = 0
    end = 0
    for i,val in enumerate(time):
        if val[0] >= end:
            result.append(val)
            start, end = val[0], val[1]
        if result:
            if result[-1][1] - result[-1][0] > val[1] - val[0]:
                result[-1]=val
                start, end = val[0], val[1]

    print('#{} {}'.format(t, len(result)))