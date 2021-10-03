# string math list | programmers 최댓값과 최솟값
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    li = sorted(list(map(int, s.split())))
    return ' '.join(map(str, [li[0], li[-1]]))