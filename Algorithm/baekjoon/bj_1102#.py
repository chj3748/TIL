# 비트마스킹 dp | bj 1102 발전소
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

sys.setrecursionlimit(int(1e9))


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
power_plants = [list(map(int, input().split())) for _ in range(N)]
onoff = 0
on_cnt = 0
for idx, stat in enumerate(input()):
    if stat == 'Y':
        onoff |= (1 << idx)  # 이진법으로 변환
        on_cnt += 1

P = int(input())
dp = [float('inf')] * (2 ** N + 1)


def turn_on(cnt, status):
    if cnt == P - on_cnt:  # 최소한으로 켜야할 발전소를 다켰으면 더 이상 비용x
        return 0
    if dp[status] != float('inf'):  # 만약 한번이라도 최소비용 계산했으면 바로 반환
        return dp[status]
    for i in range(N):
        if status & (1 << i):  # 켜진 발전소를 찾고
            for j, on_cost in enumerate(power_plants[i]):
                if i == j:
                    continue
                if not status & (1 << j):  # 꺼진 발전소를 끌때
                    temp = turn_on(cnt + 1, status | (1 << j))  # 비용 계산
                    if dp[status] > temp + on_cost:
                        dp[status] = temp + on_cost
    return dp[status]


if on_cnt == 0:
    if P > 0:
        print(-1)
    else:
        print(0)
elif on_cnt >= P:
    print(0)
else:
    answer = turn_on(0, onoff)
    print(answer)
