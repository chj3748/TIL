# set | programmers 폰켓몬
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(nums):
    from collections import Counter
    cnts = Counter(nums)
    return len(nums)//2 if len(cnts) >= len(nums)//2 else len(cnts)