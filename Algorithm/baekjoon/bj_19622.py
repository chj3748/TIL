# dp | bj 19622 회의실 배정 3
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))
dp = [0] * N

# 바텀업
for i in range(N):
    if i == 0:
        dp[0] = meetings[0][2]
    elif i == 1:
        dp[1] = max(meetings[1][2], dp[0])
    else:
        dp[i] = max(dp[i-2] + meetings[i][2], dp[i-1])

# 탑다운
# sys.setrecursionlimit(int(1e9))
#
# def find_max_people(idx):
#     if dp[idx] != 0:
#         return dp[idx]
#     if idx == 0:
#         dp[0] = meetings[0][2]
#     elif idx == 1:
#         dp[1] = max(meetings[1][2], find_max_people(0))
#     else:
#         dp[idx] = max(find_max_people(idx - 2) + meetings[idx][2], find_max_people(idx - 1))
#     return dp[idx]
# find_max_people(N - 1)

print(dp[N - 1])
