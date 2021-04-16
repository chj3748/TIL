T=int(input())
d=[
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,1),
    (1,1),
    (1,0),
    (1,-1),
    (0,-1),
]
for t in range(1,T+1):
    constellation = [list(map(int, input().split())) for _ in range(10)]
    cnt=0
    for i in range(len(constellation)):
        for j in range(len(constellation[i])):
            if constellation[i][j]==1:
                stack=[(i,j)]
                cnt+=1
                while stack:
                    p=stack.pop()
                    constellation[p[0]][p[1]]=0
                    for dm in d:
                        y=p[0]+dm[0]
                        x=p[1]+dm[1]
                        if 0<=y<10 and 0<=x<10:
                            if constellation[y][x]==1:
                                stack.append((y,x))

    print('#{} {}'.format(t, cnt))