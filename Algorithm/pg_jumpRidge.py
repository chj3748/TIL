# 효율성 실패

# def solution(stones, k):
#     answer = 0
#     check = 1
#     while check:
#         cnt = 0
#         for i,idx in enumerate(stones):
#             if idx == 0:
#                 cnt += 1
#                 if cnt >= k:
#                     check = 0
#                     break
#             else:
#                 cnt=0
#                 stones[i] -= 1
#         else:
#             answer += 1
#     return answer
#

## 이분탐색풀이
def check(mid, stones, k):
    cnt = 0
    res = -25557000000
    for v in stones:
        if v < mid:
            cnt += 1
        else:
            if cnt >= res:
                res = cnt
            cnt = 0
    else:
        if cnt >= res:
            res = cnt
    return res >= k

def solution(stones, k):
    s = 1
    e = max(stones)
    res = 0
    while s <= e:
        mid = (s + e) //2
        if check(mid, stones, k):
            e = mid - 1
        else:
            res = mid
            s = mid + 1

    return res