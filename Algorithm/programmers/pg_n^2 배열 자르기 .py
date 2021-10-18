# math | programmers n^2 배열 자르기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, left, right):
    answer = []
    l_div, l_mod = divmod(left, n)
    r_div, r_mod = divmod(right, n)
    if l_div == r_div:
        answer = ([l_div + 1] * l_div + [i + 1 for i in range(l_div, n - l_div)])[l_mod:r_mod + 1]
    else:
        for i in range(l_div, r_div + 1):
            temp = [i + 1] * i + [j + 1 for j in range(i, n)]
            if i == l_div:
                answer += temp[l_mod:]
            elif i == r_div:
                answer += temp[:r_mod + 1]
            else:
                answer += temp
    return answer