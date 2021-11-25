# dfs bfs | programmers 타겟 넘버
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(numbers, target):
    answer = 0
    l = len(numbers)

    def make_sum(idx, total):
        nonlocal answer
        if idx == l:
            if total == target:
                answer += 1
            return
        make_sum(idx + 1, total + numbers[idx])
        make_sum(idx + 1, total - numbers[idx])

    make_sum(0, 0)
    return answer