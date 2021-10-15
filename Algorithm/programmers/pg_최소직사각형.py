# math | programmers 최소직사각형
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(sizes):
    temp = list(zip(*[[min(size), max(size)] for size in sizes]))
    return max(temp[0]) * max(temp[1])