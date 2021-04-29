# 백트래킹 | bj 15664 N과M(10)
import sys
import itertools

sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

# 전형적인 순열/조합 짜는 방식으로 품
def upper_permu(cnt, sequence):
    if cnt == M:
        if sequence not in oks:
            oks.append(sequence)
    else:
        for idx, number in enumerate(numbers):
            if check[idx] == 0:
                check[idx] = 1
                if sequence:
                    if sequence[-1] <= number:
                        upper_permu(cnt + 1, sequence + [number])
                else:
                    upper_permu(cnt + 1, sequence + [number])
                check[idx] = 0


N, M = map(int, inp().split())
numbers = list(map(int, inp().split()))
check = [0] * N
oks = []

upper_permu(0, [])

oks.sort()  # 사전 순으로 정렬
for ok in oks:
    print(' '.join(map(str, ok)))
