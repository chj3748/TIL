# 문자열 구현 | bj 10809 알파벳 찾기
import sys

def input():
    return sys.stdin.readline().rstrip()


string = input()
checked = [-1] * 26
for i, s in enumerate(string):
    idx = ord(s) - ord('a')
    if checked[idx] == -1:
        checked[idx] = i

print(*checked)
