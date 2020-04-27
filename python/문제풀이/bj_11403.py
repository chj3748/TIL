# 경로찾기
n = int(input())

def bfs(y,x):
    visited=[]
    queue=[y]
    while queue:
        px=queue.pop(0)
        for idx, val in enumerate(arr[px]):
            if val==1 and idx not in visited:
                queue.append(idx)
                visited.append(idx)
                if idx==x:
                    return 1
    return 0

arr = [ list(map(int,input().split())) for _ in range(n) ]
for i in range(n):
    for j in range(n):
        if arr[i][j]==0:
            arr[i][j]=bfs(i,j)

for row in arr:
    print(' '.join(map(str,row)))
