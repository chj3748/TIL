# string | programmers JadenCase 문자열 만들기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    answer = []
    for val in s:
        if not answer or answer[-1] == ' ':
            answer.append(val.upper())
        else:
            answer.append(val.lower())
    return ''.join(answer)