# 수학 문자열 | programmers 3진법 뒤집기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def num_to_base3(n):
    base3 = []
    while n > 0:
        div, mod = divmod(n, 3)
        base3.append(mod)
        n = div
    return ''.join(map(str, base3[::-1]))


def r_base3_to_dec(str_num):
    str_num = str_num[::-1]
    total = sum([int(str_num[i]) * (3 ** (len(str_num) - i - 1)) for i in range(len(str_num))])
    return total


def solution(n):
    return r_base3_to_dec(num_to_base3(n))