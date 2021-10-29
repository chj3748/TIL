# dfs permutation | programmers 피로도
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(k, dungeons):
    answer = 0
    checked = [0] * len(dungeons)

    def go_dungeon(cnt, stress):
        nonlocal answer
        if cnt > answer:
            answer = cnt
        for idx, dungeon in enumerate(dungeons):
            if checked[idx]:
                continue
            if dungeon[0] <= stress:
                checked[idx] = 1
                go_dungeon(cnt + 1, stress - dungeon[1])
                checked[idx] = 0

    go_dungeon(0, k)
    return answer