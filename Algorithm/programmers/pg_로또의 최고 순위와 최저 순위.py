# set | programmers 로또의 최고 순위와 최저 순위
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(lottos, win_nums):
    win = [6, 6, 5, 4, 3, 2, 1]
    zero = 0
    matched = 0
    for num in lottos:
        if num == 0:
            zero += 1
        elif num in win_nums:
            matched += 1
    return [win[zero + matched], win[matched]]