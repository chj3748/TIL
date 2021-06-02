# LCS dp 문자열 | bj 9251 LCS
import sys


def input():
    return sys.stdin.readline().rstrip()


string1 = '_' + input()
string2 = '_' + input()
len1 = len(string1)
len2 = len(string2)
dp = [[0] * len2 for _ in range(len1)]

for i in range(1, len1):
    for j in range(1, len2):
        if string1[i] == string2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[len1 - 1][len2 - 1])
