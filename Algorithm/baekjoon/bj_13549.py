# 구현 bfs | bj 13549 숨박꼭질 3
import sys
from collections import deque
import math

def input():
    return sys.stdin.readline().rstrip()


N, K = map(int, input().split())
answer = 0
deq = deque()
deq.append([N, 0])
checked = [0] * 100001
checked[N] = 1
while deq:
    x, t = deq.popleft()
    if x == K:
        answer = t
        break

    if x and x <= K:
        teleport = K % x
        if not teleport:
            possible = math.log(K // x, 2)
            if not possible % 1:
                answer = t
                break
    i = 0
    while True:
        i += 1
        temp = x * (2 ** i)
        if temp > 100000 or temp == 0:
            break
        if not checked[temp]:
            deq.append([temp, t])
            checked[temp] = 1
    if 0 <= x - 1 <= 100000 and not checked[x - 1]:
        deq.append([x - 1, t + 1])
        checked[x - 1] = 1
    if 0 <= x + 1 <= 100000 and not checked[x + 1]:
        deq.append([x + 1, t + 1])
        checked[x + 1] = 1
print(answer)