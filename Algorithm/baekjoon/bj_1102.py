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
        onoff |= (1 << idx)
        on_cnt += 1

P = int(input())
dp = [float('inf')] * (2 ** N + 1)


def turn_on(cnt, status):
    if cnt == P - on_cnt:
        return 0
    if dp[status] != float('inf'):
        return dp[status]
    for i in range(N):
        if status & (1 << i):
            for j, on_cost in enumerate(power_plants[i]):
                if i == j:
                    continue
                if not status & (1 << j):
                    temp = turn_on(cnt + 1, status | (1 << j))
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
