# 그래프 dfs bfs 시뮬레이션 | programmers 가운데 글자 가져오기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    l = len(s)
    mid = l // 2
    return s[mid]if l%2 else s[mid - 1:mid + 1]