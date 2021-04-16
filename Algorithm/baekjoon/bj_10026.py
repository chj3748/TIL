dm = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0),
]
n = int(input())
bg = []
rgbg=[]
for _ in range(n):
    a= input()
    bg.append(list(a))
    rgbg.append(list(a))

# 적록 색약은 빨강 = 녹색

cnt=0
rgcnt=0

for i in range(n):
    for j in range(len(bg)):
        if bg[i][j]!=0:
            cnt+=1
            stack=[(i,j)]
            while stack:
                y,x=stack.pop(0)
                value=bg[y][x]
                bg[y][x]=0
                for d in dm:
                    if 0<=d[0]+y<n and 0<=d[1]+x<n:
                        if bg[d[0]+y][d[1]+x]== value and value!=0:
                            stack.append((d[0]+y,d[1]+x))

        if rgbg[i][j]!=0:
            rgcnt+=1
            stack=[(i,j)]
            while stack:
                y,x=stack.pop(0)
                value=rgbg[y][x]
                rgbg[y][x]=0
                for d in dm:
                    if 0<=d[0]+y<n and 0<=d[1]+x<n:
                        if value=='B':
                            if rgbg[d[0] + y][d[1] + x] == value and value!=0:
                                stack.append((d[0] + y, d[1] + x))
                        else:
                            if rgbg[d[0] + y][d[1] + x] in ('G','R') and value!=0:
                                stack.append((d[0] + y, d[1] + x))

print(cnt, rgcnt)