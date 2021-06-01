# 문자열 bf | bj 1543 문서 검색
import sys


def input():
    return sys.stdin.readline().rstrip()

string = input()
s = input()

answer = string.count(s)
print(answer)