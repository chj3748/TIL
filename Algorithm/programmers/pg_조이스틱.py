# greedy | programmers 조이스틱
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(name):
    l = len(name)
    checked = [0] * l
    cnts = [0] * l
    alpha_dict = {}
    for i in range(26):
        alpha_dict[chr(ord('A') + i)] = i
    for idx in range(l):
        c = alpha_dict[name[idx]]
        cnts[idx] = min(26 - c, c)
        if cnts[idx] == 0:
            checked[idx] = 1
    position = 0
    total = cnts[0]
    checked[0] = 1
    while True:
        left = -1
        right = -1
        for i in range(1, l):
            if not checked[(l + position - i) % l]:
                left = i
                break
        for i in range(1, l):
            if not checked[(position + i) % l]:
                right = i
                break
        if left == -1 or right == -1:
            break
        left_p = (l + position - left) % l
        right_p = (position + right) % l
        if left < right:
            position = left_p
            total += left + cnts[left_p]
            checked[left_p] = 1
        else:
            position = right_p
            total += right + cnts[right_p]
            checked[right_p] = 1
    return total