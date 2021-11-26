# hash combination | programmers 메뉴 리뉴얼
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(orders, course):
    from collections import defaultdict
    from itertools import combinations
    answer = []
    menus = defaultdict(int)
    for order in orders:
        for c in course:
            if c <= len(order):
                for combi in combinations(order, c):
                    menus[''.join(sorted(combi))] += 1
    cnts = [0] * 11
    max_menus = [[] for _ in range(11)]
    for key, val in menus.items():
        if val < 2:
            continue
        l = len(key)
        if cnts[l] < val:
            cnts[l] = val
            max_menus[l] = [''.join(key)]
        elif cnts[l] == val:
            max_menus[l].append(''.join(key))
    answer = []
    for n in course:
        answer += max_menus[n]

    return sorted(answer)