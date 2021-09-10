# 수학 | programmers 부족한 금액 계산하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(price, money, count):
    answer = price * count * (count + 1) // 2 - money
    return 0 if answer < 0 else answer