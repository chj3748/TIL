dx=[0,0,-1,1]
dy=[-1,1,0,0]
T=int(input())
for t in range(1,T+1):
    n=int(input())
    bg=[]
    si=0
    sj=0
    for i in range(n):
        a=list(map(int,input()))
        if 2 in a:
            si=i
            sj= a.index(2)
        bg.append(a)
    stack=[]
    stack.append([si,sj])
    result=-1

    while stack:
        if result==1:
            break
        y,x= stack.pop()
        bg[y][x]=5
        for i in range(4):
            if 0<=y+dy[i]<n and 0<=x+dx[i]<n:
                if bg[y+dy[i]][x+dx[i]] in [0,3]:
                    stack.append([y+dy[i],x+dx[i]])
                if bg[y+dy[i]][x+dx[i]]==3:
                    result=1
                    break
    else:
        result=0
    print('#{} {}'.format(t,result))