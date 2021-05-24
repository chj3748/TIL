# 슬라이딩윈도우 투포인터 | bj 10025 게으른 백곰
import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

zoo = [0]*1000001
max_x = 0
total = 0
for _ in range(N):
    g, x = map(int, input().split())
    zoo[x] = g
    total += g
    if max_x < x:
        max_x = x
if K >= 500000:
    print(total)
    sys.exit(0)

answer = sum(zoo[:2 * K + 1])
temp = answer
for i in range(2 * K + 1, max_x + 1):
    temp += zoo[i]
    temp -= zoo[i - (2 * K + 1)]
    if answer < temp:
        answer = temp
print(answer)
