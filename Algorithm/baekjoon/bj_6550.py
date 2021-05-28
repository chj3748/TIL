# 문자열 | bj 6550 부분 문자열
import sys


def input():
    return sys.stdin.readline().rstrip()

while True:
    value = input()
    if len(value) < 2:
        break
    string_s, string_t = value.split()
    idx_s = 0
    idx_t = 0
    while idx_t < len(string_t) and idx_s < len(string_s):
        if string_s[idx_s] == string_t[idx_t]:
            idx_s += 1
            idx_t += 1
        else:
            idx_t += 1
    if idx_s == len(string_s):
        print('Yes')
    else:
        print('No')

