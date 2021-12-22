# 순열 조합 | programmers 스타 수열
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(a):
    from collections import Counter
    answer = 0
    nums = Counter(a)

    for k in nums.keys():
        if nums[k] <= answer:
            continue
        idx = 0
        cnt = 0
        while idx < len(a) - 1:
            if a[idx] == a[idx + 1]:
                idx += 1
                continue
            if k in [a[idx], a[idx + 1]]:
                cnt += 1
                idx += 2
            else:
                idx += 1
        if answer < cnt:
            answer = cnt

    return answer * 2