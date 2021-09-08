# 문자열 regex | bj 14405 피카츄
# github.com/chj3748
import sys
import re


def input():
    return sys.stdin.readline().rstrip()


p = '^((pi)|(ka)|(chu))+$'
a = re.fullmatch(p, input())
print('YES' if a else 'NO')