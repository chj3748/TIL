# dfs | programmers 여행경로
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(tickets):
    tickets.sort()
    n = len(tickets)
    checked = [0] * n

    def dfs(city):
        for idx, ticket in enumerate(tickets):
            if not checked[idx] and ticket[0] == city:
                passed.append(ticket[1])
                checked[idx] = 1
                dfs(ticket[1])
                checked[idx] = 0
                if len(passed) == n + 1:
                    return
                else:
                    passed.pop()

    passed = ['ICN']
    dfs('ICN')
    return passed