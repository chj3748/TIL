# sort 문자열 | programmers 파일명 정렬
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(files):
    answer = []
    for f in files:
        temp = []
        h = ''
        n = ''
        tail = ''
        num_check = False
        for idx, s in enumerate(f):
            if s.isdigit():
                n += s
                num_check = True
            elif not num_check:
                h += s
            else:
                tail = f[idx:]
                break
        temp.append(h)
        temp.append(n)
        temp.append(tail)
        answer.append(temp)
    answer.sort(key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(ans) for ans in answer]