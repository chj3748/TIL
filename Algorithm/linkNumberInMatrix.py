dd=[(0,-1),(0,1),(-1,0),(1,0)]

def linkNum(y,x,idx,num=0):
    if idx==7:
        res.add(num)
    else:
        num= num*10+arr[y][x]
        for dy, dx in dd:
            ny, nx = y+dy, x+dx
            if 0<=ny<4 and 0<=nx<4:
                linkNum(ny,nx,idx+1,num)


for t in range(1,int(input())+1):
    arr= [list(map(int,input().split())) for _ in range(4)]

    res=set()
    for i in range(4):
        for j in range(4):
            linkNum(i, j, 0)

    print('#{} {}'.format(t,len(res)))
