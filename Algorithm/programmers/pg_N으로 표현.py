# dp | programmers 동적계획법
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, number):
    answer = [set() for _ in range(9)]
    answer[1] = set([n])
    if n == number:
        return 1
    for i in range(2, 9):
        mid = i // 2
        concat_num = int(str(n) * i)
        if concat_num == number:
            return i
        answer[i].add(concat_num)
        for f in range(1, mid + 1):
            s = i - f
            for f_num in answer[f]:
                for s_num in answer[s]:
                    plus_result = f_num + s_num
                    minus_result = f_num - s_num
                    r_minus_result = s_num - f_num
                    mul_result = f_num * s_num
                    div_result = 0
                    r_div_result = 0
                    if s_num:
                        div_result = f_num // s_num
                    if f_num:
                        r_div_result = s_num // f_num
                    answer[i].add(plus_result)
                    answer[i].add(minus_result)
                    answer[i].add(r_minus_result)
                    answer[i].add(mul_result)
                    answer[i].add(div_result)
                    answer[i].add(r_div_result)
                    if number in answer[i]:
                        return i
    else:
        return -1