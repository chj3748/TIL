# bj 14891 톱니바퀴
# def turn(target,d): # d 1은 시계방향 , -1은 반시계방향
#     target_gear=gears[target]
#     if d==1:
#         temp=target_gear.pop()
#         target_gear.insert(0,temp)
#     else:
#         temp=target_gear.pop(0)
#         target_gear.append(temp)
#     gears[target]=target_gear
# gears = [ list(input()) for _ in range(4) ]
# K = int(input())
# target_d_s = [ list(map(int,input().split())) for _ in range(K)]
#
# while target_d_s:
#     target,d= target_d_s.pop(0)
#     if target == 1:
#         if gears[0][2]!=gears[1][6]:
#             nextd= d*(-1)
#             if gears[1][2]!=gears[2][6]:
#                 nextd1= nextd*(-1)
#                 if gears[2][2]!=gears[3][6]:
#                     nextd2= nextd1*(-1)
#                     turn(3,nextd2)
#                 turn(2,nextd1)
#             turn(1,nextd)
#
#     elif target == 2:
#         if gears[0][2] != gears[1][6]:
#             nextd = d * (-1)
#             turn(0, nextd)
#         if gears[1][2]!=gears[2][6]:
#             nextd= d*(-1)
#             if gears[2][2]!=gears[3][6]:
#                 nextd1= nextd*(-1)
#                 turn(3,nextd1)
#             turn(2,nextd)
#
#     elif target == 3:
#         if gears[2][2] != gears[3][6]:
#             nextd = d * (-1)
#             turn(3, nextd)
#
#         if gears[1][2] != gears[2][6]:
#             nextd = d * (-1)
#             if gears[0][2] != gears[1][6]:
#                 nextd1 = nextd * (-1)
#                 turn(0, nextd1)
#             turn(1, nextd)
#
#     elif target == 4:
#         if gears[2][2] != gears[3][6]:
#             nextd = d * (-1)
#             if gears[1][2]!=gears[2][6]:
#                 nextd1= nextd*(-1)
#                 if gears[0][2]!=gears[1][6]:
#                     nextd2= nextd1*(-1)
#                     turn(0,nextd2)
#                 turn(1,nextd1)
#             turn(2, nextd)
#     turn(target-1,d)
#
# result=0
# for idx,gear in enumerate(gears):
#     if gear[0]=='1':
#         result+=(2**idx)
#
# print(result)


import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

gears = [deque(list(map(int, input()))) for _ in range(4)]
K = int(input())

def gear_rotate(target, d):
    gears[target].rotate(d)


for k in range(K):
    target, direction = map(int, input().split())
    target -= 1
    rotate_gear = deque([[target, direction, 0]])
    while rotate_gear:
        t, d, before = rotate_gear.popleft()
        if before == 0:
            if t + 1 < 4:
                if gears[t][2] != gears[t + 1][6]:
                    rotate_gear.appendleft([t + 1, d * (-1), -1])
            if t - 1 >= 0:
                if gears[t][6] != gears[t - 1][2]:
                    rotate_gear.appendleft([t - 1, d * (-1), 1])
            gear_rotate(t, d)
        elif before == -1:
            if t + 1 < 4:
                if gears[t][2] != gears[t + 1][6]:
                    rotate_gear.appendleft([t + 1, d * (-1), -1])
            gear_rotate(t, d)
        elif before == 1:
            if t - 1 >= 0:
                if gears[t][6] != gears[t - 1][2]:
                    rotate_gear.appendleft([t - 1, d * (-1), 1])
            gear_rotate(t, d)
answer = 0
for i in range(4):
    if gears[i][0]:
        answer += 2**i
print(answer)
