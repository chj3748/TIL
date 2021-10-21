# 구현 | programmers 교점에 별 만들기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(line):
    from itertools import combinations
    combis = combinations(line, 2)
    points = []
    inf = float('inf')
    min_x = inf
    max_x = -inf
    min_y = inf
    max_y = -inf
    for combi in combis:
        a, b, e = combi[0]
        c, d, f = combi[1]
        div = (a * d - b * c)
        if div == 0:
            continue
        x, y = (b * f - e * d) / div, (e * c - a * f) / div
        if not (x % 1 == 0 and y % 1 == 0):
            continue
        else:
            x, y = int(x), int(y)
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
        points.append([y, x])
    answer = [['.'] * (abs(max_x - min_x) + 1) for _ in range(abs(max_y - min_y) + 1)]
    for x, y in points:
        answer[x - min_y][y - min_x] = '*'
    answer = [''.join(row) for row in answer[::-1]]
    return answer
