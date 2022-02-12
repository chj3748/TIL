# bf 완전탐색 | baekjoon 15661 링크와 스타트
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]
min_diff = int(1e9)


def make_team(idx, team_a, status_a, team_b, status_b):
    global min_diff
    if idx == N:
        if not team_a or not team_b:
            return
        temp = abs(status_a - status_b)
        if temp < min_diff:
            min_diff = temp
        return
    add_status_a = 0
    for men_a in team_a:
        add_status_a += status[idx][men_a] + status[men_a][idx]
    make_team(idx + 1, team_a + [idx], status_a + add_status_a, team_b, status_b)
    add_status_b = 0
    for men_b in team_b:
        add_status_b += status[idx][men_b] + status[men_b][idx]
    make_team(idx + 1, team_a, status_a, team_b + [idx], status_b + add_status_b)


make_team(0, [], 0, [], 0)
print(min_diff)