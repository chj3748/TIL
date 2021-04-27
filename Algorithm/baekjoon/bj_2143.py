# 이분탐색? 누적합 | bj 2143 두 배열의 합
import sys

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

T = int(inp())
n = int(inp())
A_arr = list(map(int, inp().split()))
m = int(inp())
B_arr = list(map(int, inp().split()))

cnt = 0

# a에서 합계 구하기
acc_sum_a = [A_arr[0]] * n  # 누적합 배열 생성
for i in range(1, n):
    acc_sum_a[i] = acc_sum_a[i - 1] + A_arr[i]

a_sum = {}  #
for i in range(n):
    if a_sum.get(acc_sum_a[i]):  # 각각의 누적합은 총합이 될수 있음
        a_sum[acc_sum_a[i]] += 1
    else:
        a_sum[acc_sum_a[i]] = 1  # -----------------
    for j in range(i + 1, n):  # 뒤에 있는 누적합에서 앞에있는 누적합을 빼면 중간 누적합을 구할 수 있음
        temp = acc_sum_a[j] - acc_sum_a[i]
        if a_sum.get(temp):
            a_sum[temp] += 1
        else:
            a_sum[temp] = 1  # ---------------------------
#
# b 합계 구하기
acc_sum_b = [B_arr[0]] * m
for i in range(1, m):
    acc_sum_b[i] = acc_sum_b[i - 1] + B_arr[i]

b_sum = {}
for i in range(m):
    if b_sum.get(acc_sum_b[i]):
        b_sum[acc_sum_b[i]] += 1
    else:
        b_sum[acc_sum_b[i]] = 1
    for j in range(i + 1, m):
        temp = acc_sum_b[j] - acc_sum_b[i]
        if b_sum.get(temp):
            b_sum[temp] += 1
        else:
            b_sum[temp] = 1

# 이분탐색을 하는게 정해인데 dictionary로 접근함 O(1)
for a in a_sum:
    find_b = T - a
    if b_sum.get(find_b):
        cnt += 1 * b_sum[find_b] * a_sum[a]

print(cnt)
