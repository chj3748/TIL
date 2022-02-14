# bfs | baekjoon 5014 스타트링크
# github.com/chj3748
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


F, S, G, U, D = map(int, input().split())
checked = [0] * (F + 1)
dq = deque()
dq.append([S, 0])
checked[S] = 1
while dq:
    x, cnt = dq.popleft()
    if x == G:
        print(cnt)
        break
    if x + U <= F and not checked[x + U]:
        checked[x + U] = 1
        dq.append([x + U, cnt + 1])
    if x - D >= 1 and not checked[x - D]:
        checked[x - D] = 1
        dq.append([x - D, cnt + 1])
else:
    print('use the stairs')