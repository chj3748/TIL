# 구현 | bj 14719 빗물
# github.com/chj3748
# 조금 더 효율적으로 짤 수가 있음 O_n으로 가능하도록 생각해보자
import sys


def input():
    return sys.stdin.readline().rstrip()


H, W = map(int, input().split())
blocks = list(map(int, input().split()))
max_h = 0
min_h = 500
for val in blocks:
    if max_h < val:
        max_h = val
    if min_h > val:
        min_h = val


def goinmul(r):
    cnt = 0
    flag = False
    temp_cnt = 0
    for col in range(W):
        if blocks[col] > r:
            if flag:
                cnt += temp_cnt
                temp_cnt = 0
            else:
                flag = True
        else:
            if flag:
                temp_cnt += 1
    return cnt


total = 0
for row in range(min_h, max_h + 1):
    total += goinmul(row)

print(total)