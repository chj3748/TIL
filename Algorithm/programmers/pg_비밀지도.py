# 문자열 비트연산 | programmers 비밀지도
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, arr1, arr2):
    arr1 = [bin(val)[2:].zfill(n) for val in arr1]
    arr2 = [bin(val)[2:].zfill(n) for val in arr2]
    answer = [[' '] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                answer[i][j] = '#'
    answer = [''.join(row) for row in answer]
    return answer