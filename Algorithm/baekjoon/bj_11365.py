# 문자열 | bj 11365 !밀비 급일
import sys


def input():
    return sys.stdin.readline().rstrip()


while True:
    string = input()
    if string == 'END':
        break
    print(string[::-1])
