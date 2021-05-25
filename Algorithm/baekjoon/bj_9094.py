# 수학 | bj 9094 수학적 호기심
import sys


def input():
    return sys.stdin.readline().rstrip()


for t in range(int(input())):
    n, m = map(int, input().split())
    cnt = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if (a * a + b * b + m) % (a * b) == 0:
                cnt += 1
    print(cnt)
