# 완전탐색 | programmers 모의고사
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def match_cnt(people, answer):
    cnt = 0
    selects = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    select = selects[people]
    for idx, ans in enumerate(answer):
        if select[idx % len(select)] == ans:
            cnt += 1
    return cnt


def solution(answers):
    max_cnt = -1
    answer = []
    for i in range(1, 4):
        cnt = match_cnt(i - 1, answers)
        if cnt > max_cnt:
            max_cnt = cnt
            answer = [i]
        elif cnt == max_cnt:
            answer.append(i)

    return sorted(answer)