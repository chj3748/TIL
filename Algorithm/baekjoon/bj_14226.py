# 구현 dp bfs | bj 14226 이모티콘
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


s = int(input())
# 행 화면 갯수, 열 클립보드 갯수
dp = [[0] * 1005 for _ in range(1005)]
deq = deque()  # 화면, 클립보드, 시간
deq.append([1, 0, 0])
answer = 0
while deq:
    cnt, c, t = deq.popleft()
    if cnt == s:
        answer = t
        break
    t += 1
    if not dp[cnt][0]:
        deq.append([cnt, cnt, t])
        dp[cnt][0] = t
    if c and not dp[cnt][c]:
        deq.append([cnt + c, c, t])
    if cnt and not dp[cnt][c]:
        deq.append([cnt - 1, c, t])
    dp[cnt][c] = t
    dp[cnt][0] = 1
print(answer)