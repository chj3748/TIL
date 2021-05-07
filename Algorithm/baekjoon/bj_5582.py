# dp LCS | bj 5582 공통 부분 문자열
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
dp = [[0] * (M + 1) for _ in range(N + 1)]
# ex.
# String A = "ABCD" , String B = "AEBD"
# dp[4][4] = 1 + dp[3][3]  => 4번째 D가 같아서 최대문자열 길이가 바뀌려면
#                             3번째 문자가 같았을때 4문자가 영향을 미침
#                             즉, i번째 문자가 영향을 주려면 i-1번째 문자가 같아야함
# dp[3][3] = 0;               만약 i-1번째 문자가 다르다면 백날 뒤에 같은 문자를 더해도 영향 x
answer = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if string1[i - 1] == string2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if answer < dp[i][j]:
                answer = dp[i][j]

print(answer)
