# stack | programmers 짝지어 제거하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    stack = []
    for string in s:
        if stack:
            if string == stack[-1]:
                stack.pop()
                continue
        stack.append(string)
    return 0 if stack else 1