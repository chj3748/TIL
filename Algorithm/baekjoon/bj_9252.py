# dp LCS | bj 9252 LCS2(최장 공통 부분 수열)
import sys

# import itertools
# from math import factorial
# from collections import deque
# import heapq
# import math

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

string1 = inp().strip()
string2 = inp().strip()
N = len_str1 = len(string1)
M = len_str2 = len(string2)
dp = [[''] * (M + 1) for _ in range(N + 1)]
# ex.
# String A = "ABCD" , String B = "AEBD"
# dp[4][4] = 1 + dp[3][3]  => 4번째 D가 같으면, 3번째까지 최장 문자 순열 + 4번째 문자가 됨
#                             즉, i번째 문자가 같다면 i-1까지의 최장 순열 + 1 이다
# dp[3][3] = 2;               만약 i번째 문자가 다르다면,
#                             첫번째문자열의 i번째 문자만 더해서 최장 순열을 구한것과
#                             2번째 문자열의 i번째 문자만 더해서 최장 순열을 구한것
#                             둘중 더 큰값을 채택한다다answer = ''
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if string1[i - 1] == string2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + string2[j - 1]
        else:
            if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]
        if len(answer) < len(dp[i][j]):
            answer = dp[i][j]

print(len(answer))
print(answer)

