# dp graph dfs | bj 1103 게임

import sys

sys.setrecursionlimit(1000000)
inp = sys.stdin.readline

dm = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
]
N, M = map(int, inp().split())
board = [list(inp().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]  # 현재 칸까지 오는데 걸린 최대 카운트
visited[0][0] = 1
max_cnt = 0


def dfs(x, y, cnt):
    global max_cnt
    # 반복이 있는지 판단
    if max_cnt == -1:
        return
    # 현재 칸까지 오는데 걸린 카운트가 dp에 저장된 값보다 작거나 같으면 더 움직일 필요없음
    if dp[y][x] >= cnt + 1:
        return
    # 현재 값이 구멍인지 아닌지 판단
    val = board[y][x]
    val = int(val)
    for d in dm:  # 하-우-상-좌 순서로 탐색
        if max_cnt == -1:
            return
        dx, dy = map(lambda a: a * val, d)
        if 0 <= x + dx < M and 0 <= y + dy < N:
            # 이미 방문했었으면 루프로 판단하고 모든 함수 중지
            if visited[y + dy][x + dx] == 1:
                max_cnt = -1
                return
            # 만약 다음값이 구멍이면 여기서 검사해버림 ## 벽을 나갔을때랑 동일
            next_val = board[y + dy][x + dx]
            if next_val == 'H':
                if cnt + 1 > max_cnt:
                    max_cnt = cnt + 1
                if dp[y][x] < cnt + 1:
                    dp[y][x] = cnt + 1
                continue
            # 구멍이 아닌값이면 한칸 더 이동
            visited[y + dy][x + dx] = 1
            dfs(x + dx, y + dy, cnt + 1)
            visited[y + dy][x + dx] = 0
        else:  # 다음 좌표에서 벽 바깥으로 나갔기때문에 현재 cnt +1로 계산
            if cnt + 1 > max_cnt:
                max_cnt = cnt + 1
            if dp[y][x] < cnt + 1:
                dp[y][x] = cnt + 1


dfs(0, 0, 0)

print(max_cnt)
