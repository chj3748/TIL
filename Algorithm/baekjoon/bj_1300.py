# 이분탐색 | bj 1300 K번째 수
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
k = int(input())
s, e = 1, k
while s <= e:
    m = (s + e) // 2
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, m // i)
    if cnt < k:
        s = m + 1
    else:
        e = m - 1
print(s)
