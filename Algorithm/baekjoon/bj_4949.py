# 문자열 | bj 4949 균형잡힌 세상
import sys


def input():
    return sys.stdin.readline().rstrip()


while True:
    string = input()
    if string == '.':
        break
    stack = []
    answer = 'yes'
    for s in string:
        if s.isalpha() or s == ' ' or s == '.':
            continue
        if s == ')':
            if not stack:
                answer = 'no'
                break
            pair = stack.pop()
            if pair != '(':
                answer = 'no'
                break
        elif s == ']':
            if not stack:
                answer = 'no'
                break
            pair = stack.pop()
            if pair != '[':
                answer = 'no'
                break
        else:
            stack.append(s)
    else:
        if stack:
            answer = 'no'
    print(answer)