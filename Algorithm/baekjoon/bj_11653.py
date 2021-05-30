# 수학 소수 | bj 11653 소인수분해
import sys


def input():
    return sys.stdin.readline().rstrip()

# 소수 목록을 구하고 해당 리스트로만 나누면 좀더 빨라질 수 있음
N = int(input())
last_div = 2
while N > 1:
    for i in range(last_div, N):
        if N % i == 0:
            print(i)
            N //= i
            last_div = i
            break
    else:
        print(N)
        break