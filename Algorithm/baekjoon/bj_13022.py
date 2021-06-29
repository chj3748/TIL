# 문자열 파싱 | 13022 늑대와 올바른 단어
import sys
import re


def input():
    return sys.stdin.readline().rstrip()


string = input()
strings = string.split('fw')
answer = 0
p = re.compile('^w+o+l+f+$')


def wolf_cnt(s):
    w_cnt = 0
    o_cnt = 0
    l_cnt = 0
    f_cnt = 0
    l_s = len(s)
    for alpha in s:
        if alpha == 'w':
            w_cnt += 1
            if w_cnt > l_s // 4:
                return False
        elif alpha == 'o':
            o_cnt += 1
            if o_cnt > l_s // 4:
                return False
        elif alpha == 'l':
            l_cnt += 1
            if l_cnt > l_s // 4:
                return False
        elif alpha == 'f':
            f_cnt += 1
            if f_cnt > l_s // 4:
                return False
    return True


if len(strings) == 1:
    string = strings[0]

    if re.match(p, string):
        if wolf_cnt(string):
            answer = 1
else:
    for idx, val in enumerate(strings):
        if idx == 0:
            string = strings[idx] + 'f'
        elif idx == len(strings) - 1:
            string = 'w' + strings[idx]
        else:
            string = 'w' + strings[idx] + 'f'
        if re.match(p, string):
            if wolf_cnt(string):
                continue
        break
    else:
        answer = 1

print(answer)
