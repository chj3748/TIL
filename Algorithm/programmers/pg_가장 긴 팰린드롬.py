# string | programmers 가장 긴 팰린드롬
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    n = len(s)
    answer = 1

    def find_palin(left, right):
        while left >= 0 and right < n:
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        return right - left - 1

    for i in range(n):
        max_l = max(find_palin(i, i + 1), find_palin(i, i + 2))
        if answer < max_l:
            answer = max_l
    return answer