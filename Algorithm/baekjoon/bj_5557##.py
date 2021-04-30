# 수학 dp 조합 | bj 5557 1학년
import sys

# import itertools
# import math

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N = int(inp())
numbers = list(map(int, inp().split()))
answer = numbers.pop()


def find_pm(idx, temp):
    global cnt
    if 0 <= temp <= 20:
        if idx == N - 1:
            if temp == answer:
                cnt += 1
            return
        else:
            find_pm(idx + 1, temp + numbers[idx])
            find_pm(idx + 1, temp - numbers[idx])
    else:
        return


cnt = 0

find_pm(1, numbers[0])

print(cnt)
