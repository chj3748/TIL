# 구현 bf | bj 15779 Zigzag
import sys


def input():
    return sys.stdin.readline().rstrip()

N = int(input())
numbers = list(map(int, input().split()))
answer = 0
cnt = 0
for i in range(N - 2):
    if not (numbers[i] <= numbers[i + 1] <= numbers[i + 2]) and not (numbers[i] >= numbers[i + 1] >= numbers[i + 2]):
        cnt += 1
    else:
        cnt = 0
    if answer < cnt:
        answer = cnt

print(answer + 2)