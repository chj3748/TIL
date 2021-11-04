# LRU deque | programmers 캐시
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(cacheSize, cities):
    from collections import deque

    caches = deque([], maxlen=cacheSize)
    answer = 0
    for city in cities:
        city = city.lower()
        if city in caches:
            answer += 1
            caches.remove(city)
            caches.append(city)
        else:
            answer += 5
            caches.append(city)

    return answer