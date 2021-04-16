# bj 완전탐색? | 17114 미세먼지 안녕!
def total_dust():
    total = 2
    for row in range(R):
        total+=sum(room[row])
    return total


def dust_move():
    temp_room = [ [0]*C for _ in range(R)]
    for row in range(R):
        for col in range(C):
            if room[row][col] != -1:
                dust = room[row][col]
                m_dust = dust//5
                for d in (0,1),(1,0),(0,-1),(-1,0):
                    ny, nx = row + d[0], col + d[1]
                    if 0<=ny<R and 0<=nx<C:
                        if room[ny][nx] != -1:
                            temp_room[ny][nx]+=m_dust
                            dust -= m_dust
                temp_room[row][col]+=dust
    return temp_room


def air_clean(air_cleaner):
    ro = 0
    for position in air_cleaner:
        pre_val=0
        next_val=0
        for x in range(position[1]+1,C):
            next_val = room[position[0]][x]
            room[position[0]][x] = pre_val
            pre_val = next_val
        if ro == 0:
            for y in range(position[0]-1,-1,-1):
                next_val = room[y][C-1]
                room[y][C-1] = pre_val
                pre_val = next_val
        elif ro == 1:
            for y in range(position[0]+1,R):
                next_val = room[y][C-1]
                room[y][C-1] = pre_val
                pre_val = next_val
        if ro == 0:
            for x in range(C-2,-1,-1):
                next_val = room[0][x]
                room[0][x] = pre_val
                pre_val = next_val
        elif ro == 1:
            for x in range(C-2,-1,-1):
                next_val = room[R-1][x]
                room[R-1][x] = pre_val
                pre_val = next_val
        if ro == 0:
            for y in range(1,position[0]+1):
                next_val = room[y][0]
                room[y][0] = pre_val
                pre_val = next_val
        elif ro == 1:
            for y in range(R-2,position[0]-1,-1):
                next_val = room[y][0]
                room[y][0] = pre_val
                pre_val = next_val
        for x in range(1,position[1]):
            next_val = room[position[0]][x]
            room[position[0]][x] = pre_val
            pre_val = next_val
        ro+=1




R, C, T = map(int,input().split())
global room
room=[]
air_cleaner = []
for i in range(R):
    row = list(map(int,input().split()))
    for col in range(C):
        if row[col] == -1:
            air_cleaner.append([i,col])
    room.append(row)

for _ in range(T):
    room = dust_move()
    # print(_,'---------------------------')
    for cleaner in air_cleaner:
        room[cleaner[0]][cleaner[1]] = -1
    # for i in room:
    #     print(i)
    # print(_,'clean----------------------')
    air_clean(air_cleaner)
    for cleaner in air_cleaner:
        room[cleaner[0]][cleaner[1]] = -1
    # for i in room:
    #     print(i)

result = total_dust()

print(result)