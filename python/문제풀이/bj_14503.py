# 14503 로봇청소기
dm=[(0,-1),(1,0),(0,1),(-1,0)] # 북서남동 북동남서

def clean(y,x,look):
    global clean_cnt
    queue=[[y,x]]
    direction=look
    while queue:
        y,x=queue.pop(0)
        if room[y][x] == 0 and clean_room[y][x] != 1 :
            clean_cnt += 1
            clean_room[y][x]=1
        for next in range(3,-1,-1):
            ny,nx= y + dm[(direction+next)%4][1] , x + dm[(direction+next)%4][0]
            if 0<=ny<N and 0<=nx<M:
                if room[ny][nx]==0 and clean_room[ny][nx]!=1:
                    queue.append([ny,nx])
                    direction=(direction+next)%4
                    break
        else:
            ny, nx = y + dm[(direction+2)%4][1], x + dm[(direction+2)%4][0]
            if 0<=ny<N and 0<=nx<M:
                if room[ny][nx]==0:
                    queue.append([ny,nx])



global N,M
N, M = map(int,input().split())
r, c, d = map(int,input().split())
room = [ list(map(int,input().split())) for _ in range(N)]
clean_room = [ [4]*M for _ in range(N)]
global clean_cnt
clean_cnt=0


clean(r,c,d)

print(clean_cnt)
sum()
