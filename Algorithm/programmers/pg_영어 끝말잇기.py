# string set dict | programmers 영어 끝말잇기
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, words):
    from collections import defaultdict
    word_check = defaultdict(int)
    compare_char = words[0][0]
    for idx, word in enumerate(words):
        if word[0] != compare_char or word_check[word]:
            div, mod = divmod(idx, n)
            return [mod + 1, div + 1]
        word_check[word] += 1
        compare_char = word[-1]
    return [0, 0]