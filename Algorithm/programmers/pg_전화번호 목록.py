# hash | programmers 전화번호 목록
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(phone_book):
    from collections import defaultdict
    phone_header = defaultdict(int)
    for phone in phone_book:
        for i in range(1, len(phone)):
            phone_header[phone[:i]] += 1
    for phone in phone_book:
        if phone_header[phone] > 0:
            return False
    return True