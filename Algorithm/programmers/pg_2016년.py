# math | programmers 2016년
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(a, b):
    months = [0, 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1, 14):
        months[i] += months[i - 1]
    weeks = [ 'THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    return weeks[(months[a] + b) % 7]