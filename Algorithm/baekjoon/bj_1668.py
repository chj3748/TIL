# bf | bj 1668 트로피 진열
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
trophys = [int(input()) for _ in range(N)]
r_trophys = trophys[::-1]
l_cnt = 1
r_cnt = 1
max_height = trophys[0]
min_height = r_trophys[0]
for i in range(1, N):
    if trophys[i] > max_height:
        l_cnt += 1
        max_height = trophys[i]
    if r_trophys[i] > min_height:
        r_cnt += 1
        min_height = r_trophys[i]


print(l_cnt)
print(r_cnt)