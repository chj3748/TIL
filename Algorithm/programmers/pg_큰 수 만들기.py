# stack greedy | programmers 큰 수 만들기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack[:len(stack) - k])