# 이분탐색 | programmers 입국심사
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(n, times):
    min_time = min(times) * (n // len(times))
    answer = min_time
    max_time = max(times) * (n // len(times) + 1)
    while min_time <= max_time:
        mid = (min_time + max_time) // 2
        cnt = 0
        for t in times:
            cnt += mid // t
            if cnt >= n:
                break
        if cnt >= n:
            answer = mid
            max_time = mid - 1
        else:
            min_time = mid + 1
    return answer