# 이분탐색 해시 | bj 1920 수 찾기
# github.com/chj3748


# 풀이 1
# import sys
# import bisect
#
# inp = sys.stdin.readline
#
# N = int(inp())
# arr = list(map(int, inp().split()))
# M = int(inp())
#
# arr.sort()
# find_number = list(map(int, inp().split()))
# for f_number in find_number:
#     idx = bisect.bisect_left(arr, f_number)
#     if not (arr[0] <= f_number <= arr[-1]):
#         print(0)
#     elif arr[idx] == f_number:
#         print(1)
#     else:
#         print(0)

# 새로운 풀이
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
numbers = defaultdict(int)
for num in list(map(int, input().split())):
    numbers[num] = 1

M = int(input())
for find_num in list(map(int, input().split())):
    print(1 if numbers[find_num] else 0)
