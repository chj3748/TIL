# bitwise math | programmers 두개 이하로 다른 비트
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(numbers):
    answer = []
    for number in numbers:
        temp = list(bin(number)[2:])
        zero = -1
        for idx, val in enumerate(temp[::-1]):
            if val == '0':
                zero = len(temp) - 1 - idx
                break
        if zero > -1:
            temp[zero] = '1'
            if zero + 1 < len(temp):
                temp[zero + 1] = '0'
        else:
            temp = ['1'] + temp
            temp[1] = '0'
        answer.append(int(''.join(temp), 2))
    return answer