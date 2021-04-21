# 이분탐색 | bj 1920 수 찾기
import sys
import bisect

inp = sys.stdin.readline

N = int(inp())
arr = list(map(int, inp().split()))
M = int(inp())

# O(logn)
arr.sort()
find_number = list(map(int, inp().split()))
for f_number in find_number:
    idx = bisect.bisect_left(arr, f_number)
    # print(idx, f_number, arr)
    if not (arr[0] <= f_number <= arr[-1]):
        print(0)
    elif arr[idx] == f_number:
        print(1)
    else:
        print(0)

# # O(n)
# for f_number in find_number:
#     if f_number in arr:
#         print(1)
#     else:
#         print(0)