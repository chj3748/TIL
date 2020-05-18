# 테트로미노
def tetromino(y, x, k, sum4):
    global max_sum
    if k==3:
        max_sum=max(sum4,max_sum)
        return
    for d in (1, 0), (-1, 0), (0, 1), (0, -1):
        ni, nj = y + d[0], x + d[1]
        if 0 <= ni < n and 0 <= nj < m:
            if cnt[ni][nj]==0:
                cnt[ni][nj]=1
                tetromino(ni, nj, k + 1, sum4 + paper[ni][nj])
                cnt[ni][nj]=0
    if k==1:
        temp=[]
        for d in (1,0),(-1,0),(0,1),(0,-1):
            ni, nj = y + d[0], x + d[1]
            if 0<=ni<n and 0<=nj<m:
                if cnt[ni][nj] == 0:
                    temp.append(paper[ni][nj])
        while len(temp)>2:
            temp.remove(min(temp))
        if len(temp)==2:
            tetromino(ni, nj, k + 2, sum4 + sum(temp))

                    # cnt[ni][nj] = 1
                    # for dd in (1, 0), (-1, 0), (0, 1), (0, -1):
                    #     if dd != d:
                    #         ni2, nj2 = y + dd[0], x + dd[1]
                    #         if 0 <= ni2 < n and 0 <= nj2 < m:
                    #             if cnt[ni2][nj2] == 0:
                    #                 cnt[ni2][nj2] = 1
                    #                 tetromino(ni2, nj2, k + 2, sum4 + paper[ni][nj]+paper[ni2][nj2])
                    #                 cnt[ni2][nj2] = 0
                    # cnt[ni][nj] = 0


n, m = map(int, input().split())
paper = [ list(map(int,input().split())) for _ in range(n) ]
cnt = [ [0]*m for col in range(n)]

global max_sum
max_sum = 0

for i in range(n):
    for j in range(m):
        cnt[i][j]=1
        tetromino(i,j,0,paper[i][j])
        cnt[i][j]=0

print(max_sum)