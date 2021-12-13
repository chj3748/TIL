# hash heap 우선순위큐 | programmers 베스트앨범
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(genres, plays):
    from collections import defaultdict
    import heapq
    hq = []
    genre = defaultdict(lambda: [0, []])
    for i in range(len(genres)):
        g, p = genres[i], plays[i]
        genre[g][0] += p
        heapq.heappush(genre[g][1], [-p, i])

    for k in genre.keys():
        heapq.heappush(hq, [-genre[k][0], k])

    answer = []
    while hq:
        total_play, g = heapq.heappop(hq)
        l = 2 if len(genre[g][1]) > 1 else 1
        for i in range(l):
            p, idx = heapq.heappop(genre[g][1])
            answer.append(idx)
    return answer