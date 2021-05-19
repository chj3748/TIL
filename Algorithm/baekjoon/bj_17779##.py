# dp 수학 | bj 17779 게리맨더링 2
# 풀긴했지만 시간복잡도 개선하자
import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


# 0 < d1 <= y - 1
# 0< d2 <= N - y
# 0 < d1 + d2 <= N - x
# 최대, 최소 인구수 차이의 최소값은?

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find_1(x, y, d1, d2):
    q = deque([[0, 0]])
    dp[0][0] = 1
    people1 = city[0][0]
    while q:
        section = q.popleft()
        for d in zip(dx, dy):
            nx, ny = section[0] + d[0], section[1] + d[1]
            if 0 <= nx < x + d1 and 0 <= ny <= y:
                if dp[nx][ny] != 5 and dp[nx][ny] != 1:
                    q.append([nx, ny])
                    dp[nx][ny] = 1
                    people1 += city[nx][ny]
    return people1


def find_2(x, y, d1, d2):
    q = deque([[0, N - 1]])
    dp[0][N - 1] = 2
    people2 = city[0][N - 1]
    while q:
        section = q.popleft()
        for d in zip(dx, dy):
            nx, ny = section[0] + d[0], section[1] + d[1]
            if 0 <= nx <= x + d2 and y < ny < N:
                if dp[nx][ny] != 5 and dp[nx][ny] != 2:
                    q.append([nx, ny])
                    dp[nx][ny] = 2
                    people2 += city[nx][ny]
    return people2


def find_3(x, y, d1, d2):
    q = deque([[N - 1, 0]])
    dp[N - 1][0] = 3
    people3 = city[N - 1][0]
    while q:
        section = q.popleft()
        for d in zip(dx, dy):
            nx, ny = section[0] + d[0], section[1] + d[1]
            if x + d1 <= nx < N and 0 <= ny < y - d1 + d2:
                if dp[nx][ny] != 5 and dp[nx][ny] != 3:
                    q.append([nx, ny])
                    dp[nx][ny] = 3
                    people3 += city[nx][ny]
    return people3


def find_4(x, y, d1, d2):
    q = deque([[N - 1, N - 1]])
    dp[N - 1][N - 1] = 4
    people4 = city[N - 1][N - 1]
    while q:
        section = q.popleft()
        for d in zip(dx, dy):
            nx, ny = section[0] + d[0], section[1] + d[1]
            if x + d2 < nx < N and y - d1 + d2 <= ny < N:
                if dp[nx][ny] != 5 and dp[nx][ny] != 4:
                    q.append([nx, ny])
                    dp[nx][ny] = 4
                    people4 += city[nx][ny]
    return people4


N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')
total = sum(sum(city, []))
for x in range(N):
    for y in range(N):
        for d1 in range(N):
            for d2 in range(N):
                if not (
                        d1 >= 1 and d2 >= 1 and 0 <= x < x + d1 + d2 < N and 0 <= y - d1 < y < y + d2 < N):
                    continue
                dp = [[0] * (N) for _ in range(N)]
                # 경계선 먼저 그리기
                for b1 in range(d1 + 1):
                    dp[x + b1][y - b1] = 5
                    dp[x + d2 + b1][y + d2 - b1] = 5
                for b2 in range(d2 + 1):
                    dp[x + b2][y + b2] = 5
                    dp[x + d1 + b2][y - d1 + b2] = 5
                cnt1 = find_1(x, y, d1, d2)
                cnt2 = find_2(x, y, d1, d2)
                cnt3 = find_3(x, y, d1, d2)
                cnt4 = find_4(x, y, d1, d2)
                cnt5 = total - cnt1 - cnt2 - cnt3 - cnt4
                max_v = max(cnt1, cnt2, cnt3, cnt4, cnt5)
                min_v = min(cnt1, cnt2, cnt3, cnt4, cnt5)
                if answer > max_v - min_v:
                    answer = max_v - min_v
print(answer)
