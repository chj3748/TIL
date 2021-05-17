# 누적합 dp | bj 4097 수익
import sys

# sys.setrecursionlimit(int(1e9))

def input():
    return sys.stdin.readline().rstrip()


while True:
    N = int(input())
    if not N:
        break
    revenues = []
    answer = float('-inf')
    for i in range(N):
        val = int(input())
        if not revenues:
            revenues.append(val)
        else:
            temp = revenues[i - 1] + val
            if temp < val:
                temp = val
            revenues.append(temp)
        if answer < revenues[i]:
            answer = revenues[i]
    print(answer)
