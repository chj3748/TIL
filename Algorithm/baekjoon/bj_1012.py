dm = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]
T=int(input())
for t in range(1,T+1):
    m, n, k = map(int, input().split())
    arr = [[0 for col in range(m)] for row in range(n)]

    for cabbage in range(k):
        x,y=map(int, input().split())
        arr[y][x]=1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                stack = [[i, j]]
                while stack:
                    y, x = stack.pop()
                    arr[y][x]=0
                    for d in dm:
                        ny, nx=[y+d[0],x+d[1]]
                        if 0<=ny<n and 0<=nx<m and arr[ny][nx]==1:
                            stack.append([ny,nx])


    print(cnt)