# 구현 | bj 9081 단어 맞추기
import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    answer = input()
    string = list(answer)
    sort_s = sorted(string, reverse=1)
    if string == sort_s:
        print(answer)
    else:
        sign = False
        for idx1 in range(len(string) - 2, -1, -1):
            if sign:
                break
            for idx2 in range(len(string) - 1,idx1, -1):
                if string[idx2] > string[idx1]:
                    a = string[idx1:]
                    a.remove(string[idx2])
                    a.sort()
                    answer = ''.join((*string[:idx1], string[idx2], *a))
                    sign = True
                    break
        print(answer)