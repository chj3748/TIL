# dp bf 재귀 | bj 19947 투자의 귀재 배주형
import sys
import heapq


def input():
    return sys.stdin.readline().rstrip()


# 1년 5%, 3년 20%, 5년 35% 이율
# Y년 후 최대 자산은?
H, Y = map(int, input().split())

# # 재귀
# dp = [0] * (Y + 1)
# dp[0] = H
#
# def copy_money(year):
#     if dp[year] != 0:
#         return dp[year]
#     print(year)
#     money1 = money3 = money5 = 0
#     if year - 1 >= 0:
#         money1 = copy_money(year - 1) * 1.05
#     if year - 3 >= 0:
#         money3 = copy_money(year - 3) * 1.2
#     if year - 5 >= 0:
#         money5 = copy_money(year - 5) * 1.35
#     dp[year] = int(max(money1, money3, money5) // 1)
#     return dp[year]
#
# answer = copy_money(Y)
# print(answer)

# bf
dp = [0]*(Y + 1)
dp[0] = H
for y in range(Y + 1):
    for y_cost, interest in [(1, 1.05,), (3, 1.2), (5, 1.35)]:
        if y + y_cost < Y:
            if dp[y + y_cost] < dp[y]*interest:
                dp[y + y_cost] = dp[y] * interest // 1

answer = int(dp[Y])
print(answer)
