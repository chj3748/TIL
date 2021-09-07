# 정렬 | programmers 복서 정렬하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(weights, head2head):
    import heapq
    l = len(weights)
    total_game = [0] * l
    win_game = [0] * l
    heavy_win = [0] * l
    for i in range(l):
        for j in range(i + 1, l):
            game_result = head2head[i][j]
            if game_result in 'WL':
                total_game[i] += 1
                total_game[j] += 1
                if game_result == 'W':
                    win_game[i] += 1
                    if weights[i] < weights[j]:
                        heavy_win[i] += 1
                else:
                    win_game[j] += 1
                    if weights[i] > weights[j]:
                        heavy_win[j] += 1
    hq = []
    for i in range(l):
        rate = win_game[i]/total_game[i] if total_game[i] else 0
        heapq.heappush(hq, [[-rate, -heavy_win[i], -weights[i], i], i])
    answer = []
    while hq:
        answer.append(heapq.heappop(hq)[-1] + 1)
    return answer