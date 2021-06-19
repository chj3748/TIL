# 이분탐색 | bj 15732 도토리 숨기기
import sys


def input():
    return sys.stdin.readline().rstrip()


N, K, D = map(int, input().split())
rules = []
for _ in range(K):
    s, e, j = map(int, input().split())
    rules.append([s, e, j])
answer = 0


def dotori_cnt(idx):
    cnt = 0
    for rule in rules:
        start, end, jump = rule
        if start > idx:
            continue
        if idx > end:
            cnt += (end - start) // jump + 1
        else:
            cnt += (idx - start) // jump + 1
    return cnt


def bi_search(s, e):
    global answer
    mid = (s + e) // 2
    if s > e:
        answer = mid + 1
        return
    temp = dotori_cnt(mid)
    if temp >= D:
        bi_search(s, mid - 1)
    else:
        bi_search(mid + 1, e)


bi_search(1, N)
print(answer)
