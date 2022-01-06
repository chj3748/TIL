# union-find | programmers 호텔 방 배정
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


import sys

sys.setrecursionlimit(200010)


def solution(k, room_number):
    from collections import defaultdict
    rooms = defaultdict(int)
    answer = []

    def find_r(x):
        if not rooms[x]:
            rooms[x] = x + 1
            return x
        temp = find_r(rooms[x])
        rooms[x] = temp + 1
        return temp

    for r in room_number:
        answer.append(find_r(r))
    return answer