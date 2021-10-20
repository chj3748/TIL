# str binary | programmers 이진 변환 반복하기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    answer = [0, 0]
    while s != '1':
        before_l = len(s)
        temp_s = ''
        for string in s:
            if string == '1':
                temp_s += '1'
        else:
            s = temp_s
        after_l = len(s)
        answer[0] += 1
        answer[1] += before_l - after_l
        s = bin(len(s))[2:]
    return answer


solution("110010101001")