# 투포인터 | bj 1806 부분합
import sys

# sys.setrecursionlimit(10 ** 9)
inp = sys.stdin.readline

N, S = map(int, inp().split())
numbers = list(map(int, inp().split()))

if sum(numbers) < S:
    print(0)
    sys.exit()

p1 = 0
p2 = 0
temp = numbers[0] # 일단 0번째 값을 가지고 시작하니까 두번째포인터는 0번인덱스
min_len = N
while p1 <= p2 <= N -1: # 앞조건이 발생할 일은 없는것 같음 p2가 끝에 도달해도 p1이 따라오는경우가 있으니 범위는 최대 인덱스까지
    if temp >= S:
        if min_len > p2-p1 + 1:
            min_len = p2 - p1 + 1
        temp -= numbers[p1] # 합이 크면 앞에서 빼봄
        p1 += 1
        # print(temp, p1, p2)
    else: # 합이 작으면 뒤에서 더함
        if p2 == N -1: # 그런데 인덱스 이상의 값은 더할수 없음
            break
        p2 += 1
        temp += numbers[p2]
        # print(temp, p1, p2)

print(min_len)