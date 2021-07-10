# 그리디 정렬 | bj 11399 ATM
# github.com/chj3748
import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
times = list(map(int, input().split()))
times.sort()
total = 0
for t in times:
    total += N * t
    N -= 1

print(total)