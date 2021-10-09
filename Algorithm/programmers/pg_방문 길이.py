# set graph | programmers 방문 길이
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(dirs):
    from collections import defaultdict
    checked = defaultdict(int)
    answer = 0
    ulrd = {
        'U': 0,
        'L': 1,
        'R': 2,
        'D': 3
    }

    dm = [[0, -1], [-1, 0], [1, 0], [0, 1]]
    cur_x, cur_y = 5, 5
    for d in dirs:
        nx, ny = cur_x + dm[ulrd[d]][0], cur_y + dm[ulrd[d]][1]
        if not (0 <= nx <= 10 and 0 <= ny <= 10):
            continue
        if not (checked[f'{cur_x} {cur_y} {nx} {ny}'] or checked[f'{nx} {ny} {cur_x} {cur_y}']):
            answer += 1
            checked[f'{cur_x} {cur_y} {nx} {ny}'] = 1
            checked[f'{nx} {ny} {cur_x} {cur_y}'] = 1
        cur_x, cur_y = nx, ny
    return answer