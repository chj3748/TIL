# 문자열 구현 정렬 | bj 20210 파일 탐색기
# github.com/chj3748
import sys
from functools import cmp_to_key


def input():
    return sys.stdin.readline().rstrip()


# 새로운 우선순위 사전
s_dict = {}
for idx in range(97, 123):
    s_dict[chr(idx)] = (idx - 97) * 2 + 1

for idx in range(65, 91):
    s_dict[chr(idx)] = (idx - 65) * 2

N = int(input())
strings = []
for _ in range(N):  # 입력 문자열 처리중 ex) Foo00012Bar 변환후 [['F', 'o', 'o', '00012', 'B', 'a', 'r'], [3]]
    string = input()
    temp = []
    temp_num = ''
    zero_cnt = 0
    zero = True
    zeros = []
    for s in string:
        if s.isalpha():
            if temp_num:
                temp.append(temp_num)
                zeros.append(zero_cnt)
                temp_num = ''
                zero_cnt = 0
                zero = True
            temp.append(s)
        else:
            if s == '0':
                if zero:
                    zero_cnt += 1
            else:
                zero = False
            temp_num += s
    else:
        if temp_num:
            temp.append(temp_num)
            zeros.append(zero_cnt)
    strings.append([temp, zeros])


def compare_xy(x, y):
    x_s, x_z = x
    y_s, y_z = y
    x_l = len(x_s)
    y_l = len(y_s)
    x_idx = 0
    y_idx = 0
    x_nidx = 0
    y_nidx = 0
    while x_idx != x_l and y_idx != y_l:
        if x_s[x_idx].isalpha():
            if y_s[y_idx].isalpha():  # 둘다 문자
                if x_s[x_idx] == y_s[y_idx]:
                    pass
                else:
                    if s_dict[x_s[x_idx]] < s_dict[y_s[y_idx]]:
                        return -1
                    else:
                        return 1
            else:  # x문자 y 숫자
                return 1
        else:
            if y_s[y_idx].isalpha():  # x숫자 y문자
                return -1
            else:  # 둘다 숫자
                if int(x_s[x_idx]) == int(y_s[y_idx]):
                    if x_z[x_nidx] == y_z[y_nidx]:  # 0의 갯수가 같은 경우
                        pass
                    elif x_z[x_nidx] < y_z[y_nidx]:  # x의 0갯수가 더 적은경우
                        return -1
                    else:  # y의 0 갯수가 더 적은경우
                        return 1
                    x_nidx += 1
                    y_nidx += 1
                else:
                    if int(x_s[x_idx]) < int(y_s[y_idx]):
                        return -1
                    else:
                        return 1
        x_idx += 1
        y_idx += 1
    if x_idx == x_l:
        return -1
    elif y_idx == y_l:
        return 1


answer = sorted(strings, key=cmp_to_key(compare_xy))
for ans in answer:
    print(''.join(ans[0]))

