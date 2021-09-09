# 문자열 | programmers 직업군 추천하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(table, languages, preference):
    from collections import defaultdict
    lang_prefer = defaultdict(int)
    for i in range(len(languages)):
        lang_prefer[languages[i]] = preference[i]

    types = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]

    import heapq
    hq = []
    for i, row in enumerate(table):
        total = 0
        for j, col in enumerate(row.split(' ')[1:]):
            if lang_prefer[col]:
                total += (5 - j) * lang_prefer[col]
        heapq.heappush(hq, [-total, types[i]])
    return heapq.heappop(hq)[1]