# 문자열 | bj 1152 단어의 개수
import sys


def input():
    return sys.stdin.readline().rstrip()

# strings = input().split()
# print(len(strings))

cnt = 0
sign = 0
for s in input():
    if s == ' ':
        sign = 0
    else:
        if sign == 0:
            cnt += 1
            sign = 1
print(cnt)