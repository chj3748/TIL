from copy import deepcopy
from collections import deque
dm = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]

def effect(tomatos, yt_count):
    change = True
    day = 0
    while change:
        next_tomatos = []
        day+=1
        change=False
        while tomatos:
            t = tomatos.pop()
            x,y = t
            for d in dm:
                nx, ny = x+d[0] , y+d[1]
                if 0 <= nx < n and 0 <= ny < m:
                    value= arr[nx][ny]
                    if value == 0:
                        change = True
                        yt_count-=1
                        if yt_count==0:
                            return day
                        arr[nx][ny]=1
                        next_tomatos.append((nx,ny))
        tomatos=next_tomatos
    return -1

m, n = map(int,input().split())
arr = [ list(map(int,input().split())) for _ in range(n) ]
tomato=[]
yt_cnt=0
t_cnt=0
empty_cnt=0
for i in range(n):
    for j in range(m):
        v = arr[i][j]
        if v ==0:
           yt_cnt+=1
        elif v == 1:
            t_cnt+=1
            tomato.append((i,j))
        elif v == -1:
            empty_cnt+=1
if t_cnt==0:
    print(-1)
elif (t_cnt + empty_cnt) == (n*m):
    print(0)
else:
    print(effect(tomato,yt_cnt))

# def possible():
#     temp=deepcopy(maps)
#     tomato=0
#     area=0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j]>=0:
#                 if temp[i][j]==1:
#                     tomato+=1
#                 area+=1
#                 queue=deque()
#                 queue.append([i,j])
#                 temp[i][j] = -1
#                 while queue:
#                     y, x = queue.pop()
#                     for d in dm:
#                         ny,nx = y+d[0],x+d[1]
#                         if 0<=ny<n and 0<=nx<m:
#                             if temp[ny][nx] >=0:
#                                 queue.append((ny,nx))
#                                 if temp[ny][nx]==1:
#                                     tomato+=1
#                                 temp[ny][nx]=-1
#     if area >1 or tomato==0:
#         return False
#     return True
#
#
# def effect(day):
#     v=False
#     for i in range(n):
#         for j in range(m):
#             if maps[i][j]==day+1:
#                 for d in dm:
#                     ny, nx = i + d[0], j + d[1]
#                     if 0 <= ny < n and 0 <= nx < m:
#                         if maps[ny][nx] == 0:
#                             temp.append([ny,nx])
#                             v=True
#     return v
#
# m, n = map(int,input().split())
# maps = [ list(map(int,input().split())) for _ in range(n) ]
# day = 0
# while True:
#     if day==0:
#         if not possible():
#             day=-1
#             break
#     temp=[]
#     stop = effect(day)
#     if stop==False:
#         break
#     day+=1
#     for y,x in temp:
#         maps[y][x]=day+1
# print(day)