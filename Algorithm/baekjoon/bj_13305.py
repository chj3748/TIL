# 그리디 | bj 13305 주유소
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))
total = 0
pay = costs[0]
for i in range(1, N):
    total += pay * roads[i - 1]
    if pay > costs[i]:
        pay = costs[i]

print(total)
