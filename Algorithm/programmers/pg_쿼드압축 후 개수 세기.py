# 재귀 누적합 이진탐색 | programmers 쿼드압축 후 개수 세기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(arr):
    answer = [0, 0]

    def quad_search(x, y, n):
        temp = [0, 0]
        mid = n // 2
        if mid == 0:
            temp[arr[x][y]] += 1
            return temp
        val1 = quad_search(x, y, mid)
        val2 = quad_search(x + mid, y, mid)
        val3 = quad_search(x, y + mid, mid)
        val4 = quad_search(x + mid, y + mid, mid)
        if val1 == val2 == val3 == val4 and (val1 == [0, 1] or val1 == [1, 0]):
            return val1
        else:
            for zero, one in (val1, val2, val3, val4):
                temp[0] += zero
                temp[1] += one
            return temp

    if len(arr) == 1:
        answer[arr[0][0]] += 1
    else:
        answer = quad_search(0, 0, len(arr))
    return answer