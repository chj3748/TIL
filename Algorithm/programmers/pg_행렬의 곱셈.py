# math list | programmers 행렬의 곱셈
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += arr1[i][k] * arr2[k][j]
            answer[i][j] = temp
    return answer