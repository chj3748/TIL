dm=[
    [1,0],
    [0,1],
    [-1,0],
    [0,-1],
]
m, n, k = map(int, input().split())
arr = [ [0 for x in range(n)] for y in range(m)]

for _ in range(k):
    lx,ly,rx,ry=map(int, input().split())
    for y in range(ly,ry):
        for x in range(lx,rx):
            arr[y][x]=1
result=[]
for y in range(m):
    for x in range(n):
        if arr[y][x]==0:
            cnt=0
            stack=[(y,x)]
            while stack:
                cy,cx= stack.pop()
                cnt+=1
                arr[cy][cx]=1
                for d in dm:
                    ny,nx=cy+d[0],cx+d[1]
                    if 0<=ny<m and 0<=nx<n:
                        if arr[ny][nx]==0 and [ny,nx] not in stack:
                            stack.append([ny,nx])
            else:
                result.append(cnt)
result.sort()
print(len(result))
print(' '.join(map(str,result)))