# string stack | programmers 문자열 압축
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        temp = ''
        slice_s = s[0 : i]
        cnt = 1
        idx = i
        while idx < len(s):
            if answer <= len(temp):
                break
            temp_s = s[idx:idx + i]
            idx += i
            if temp_s == slice_s:
                cnt += 1
            else:
                temp += str(cnt) + slice_s if cnt > 1 else slice_s
                cnt = 1
                slice_s = temp_s
        else:
            temp += str(cnt) + slice_s if cnt > 1 else slice_s
            if answer > len(temp):
                answer = len(temp)
    return answer