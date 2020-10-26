# swea dp | 1247 최적경로
def move(start, togo, move_d, cnt):
    global distance
    if move_d >= distance:
        return
    if cnt == N:
        move_d = move_d + abs(start[0] - home[0]) + abs(start[1] - home[1])
        if move_d < distance:
            distance = move_d
            return
    else:
        for idx, Next in enumerate(togo):
            if visited[idx] == 0:
                d = abs(start[0] - Next[0]) + abs(start[1] - Next[1])
                visited[idx] = 1
                move(Next, togo, move_d + d, cnt + 1)
                visited[idx] = 0

        # for idx, Next in enumerate(togo):
        #     if idx not in gone:
        #         d = abs(start[0] - Next[0]) + abs(start[1] - Next[1])
        #         move(Next, togo, gone+[idx], move_d + d, cnt + 1)

        # i = len(togo)
        # while i>0:
        #     Next = togo.pop(0)
        #     d = abs(start[0]-Next[0])+abs(start[1]-Next[1])
        #     move(Next, togo, gone, move_d+d, cnt+1)
        #     togo.append(Next)
        #     i-=1


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    customers = []

    # office = data[:2]
    # home = data[2:4]
    # else_data = data[4:]

    for i in range(N + 2):
        if i == 0:
            office = (data[0], data[1])
        elif i == 1:
            home = (data[2], data[3])
        else:
            customers.append((data[2 * i], data[(2 * i) + 1]))

    distance = 20000
    visited = [0] * N
    move(office, customers, 0, 0)

    print('#{} {}'.format(t, distance))

#
# # swea dp | 1247 최적경로
# def move(start, move_d, cnt):
#     global distance
#     if move_d >= distance:
#         return
#     if cnt == N:
#         move_d = move_d + distance_list[start][N + 1]
#         if move_d < distance:
#             distance = move_d
#             return
#     else:
#         for idx in range(1, N + 1):
#             if visited[idx] == 0:
#                 visited[idx] = 1
#                 move(idx, move_d + distance_list[start][idx], cnt + 1)
#                 visited[idx] = 0
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     data = list(map(int, input().split()))
#     set_list = []
#
#     for i in range(N + 2):
#         if i == 0:
#             set_list.append((data[0], data[1]))
#         elif i == 1:
#             home = (data[2], data[3])
#         else:
#             set_list.append((data[2 * i], data[(2 * i) + 1]))
#     set_list.append(home)
#     distance_list = [[0] * (N + 2) for _ in range(N + 2)]
#     distance = 0
#     visited = [0] * (N + 2)
#     for i in range(N + 2):
#         for j in range(N + 2):
#             distance_list[i][j] = abs(set_list[i][0] - set_list[j][0]) + abs(set_list[i][1] - set_list[j][1])
#     for i in range(N + 1):
#         distance += distance_list[i][i + 1]
#     visited[0] = 1
#     move(0, 0, 0)
#
#     print('#{} {}'.format(t, distance))