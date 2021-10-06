# stack | programmers 올바른 괄호
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    stack = []
    for val in s:
        if not stack:
            stack.append(val)
        else:
            if val == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    break
            else:
                stack.append(val)
    return False if stack else True