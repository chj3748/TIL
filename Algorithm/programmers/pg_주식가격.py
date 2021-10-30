# stack queue | programmers 주식가격
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(prices):
    l = len(prices)
    answer = [ i for i in range (l - 1, -1, -1)]
    stack = [0]
    for i in range (1, l):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer