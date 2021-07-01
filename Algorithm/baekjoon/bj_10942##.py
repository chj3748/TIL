# dp manacher | bj 10942 팰린드롬?
# github.com/chj3748
# manacher 이해안감...
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
temp_num = input().split()
numbers = ['*' if i % 2 else temp_num[i // 2] for i in range(n * 2)]
dp = [0] * (2 * n)


def manacher(li, l):
    r = 0
    p = 0
    for i in range(l):
        if i <= r:
            dp[i] = min(dp[2 * p - i], r - i)
        else:
            dp[i] = 0
        while i - dp[i] - 1 >= 0 and i + dp[i] + 1 < l and li[i - dp[i] - 1] == li[i + dp[i] + 1]:
            dp[i] += 1
        if r < i + dp[i]:
            r = i + dp[i]
            p = i


manacher(numbers, len(numbers))
#
# print()
# print(numbers)
# print(dp)

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    s -= 1
    e -= 1
    s *= 2
    e *= 2
    mid = (s + e) // 2
    # print(s, e, mid, 11111111)
    if dp[mid] >= mid - s:
        print(1)
    else:
        print(0)
