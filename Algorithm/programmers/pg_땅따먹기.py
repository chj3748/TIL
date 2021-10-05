# dp | programmers 땅따먹기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(land):
    for r in range(1, len(land)):
        sorted_before = sorted(enumerate(land[r - 1]), key = lambda x:x[1])
        last_idx, last_val = sorted_before[-1]
        second_idx, second_val = sorted_before[-2]
        for c in range(4):
            land[r][c] += second_val if last_idx == c else last_val
    return max(land[-1])