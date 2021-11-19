# 이분탐색 | programmers 순위 검색
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(info, query):
    from collections import defaultdict
    answer = []
    infos = defaultdict(list)
    for applicant in info:
        lang, position, year, food, point = applicant.split(' ')
        point = int(point)
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        tlang = '-' if a else lang
                        tposition = '-' if b else position
                        tyear = '-' if c else year
                        tfood = '-' if d else food
                        infos[tlang, tposition, tyear, tfood].append(point)

    for k in infos.keys():
        infos[k].sort()

    for q in query:
        q_split = q.split(' ')
        lang, position, year, food, point = q_split[0], q_split[2], q_split[4], q_split[6], int(q_split[7])
        info = infos[lang, position, year, food]
        start, end = 0, len(info) - 1
        while start <= end:
            mid = (start + end) // 2
            if info[mid] < point:
                start = mid + 1
            else:
                end = mid - 1
        answer.append(len(info) - start)
    return answer