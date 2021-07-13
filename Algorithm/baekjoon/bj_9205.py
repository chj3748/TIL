# 플로이드워셜 그래프 bfs | bj 9205 맥주 마시면서 걸어가기
# github.com/chj3748
# 플로이드 워셜로 풀었는데, 중간에 각 지점까지 이동가능 유무를 구한후 bfs로 실행하면 훨씬 빠르게 끝낼수 있음
import sys

def input():
    return sys.stdin.readline().rstrip()


t = int(input())
for tn in range(1, t + 1):
    n = int(input())
    paths = []
    for _ in range(n + 2):  # [시작점, *편의점, 도착점]
        paths.append(list(map(int, input().split())))
    inf = float('inf')
    dist = [[inf] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                continue
            diff = abs(paths[i][0] - paths[j][0]) + abs(paths[i][1] - paths[j][1])
            if diff <= 1000:
                dist[i][j] = 1
    for k in range(n + 2):  # 경유지 번호
        for i in range(n + 2):  # 시작점 번호
            for j in range(n + 2):  # 도착점 번호
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    if dist[0][n + 1] == inf:
        print('sad')
    else:
        print('happy')