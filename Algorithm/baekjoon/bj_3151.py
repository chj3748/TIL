# bf 투포인터 정렬 | baekjoon 3151 합이 0
# github.com/chj3748
import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
numbers = list(map(int, input().split()))
cnt_number = defaultdict(int)
for number in numbers:
    cnt_number[number] += 1

answer = 0
numbers = sorted(list(cnt_number.keys()))
div = [1, 2, 6, 6]
N = len(numbers)
for f in range(N):
    num1 = numbers[f]
    for s in range(f, N):
        num2 = numbers[s]
        same = 0
        cnt_num1 = cnt_number[num1]
        cnt_num2 = cnt_number[num2]
        if num1 == num2:
            cnt_num2 -= 1
            same += 1
        temp = -(num1 + num2)
        if temp < num2:
            continue
        cnt_temp = cnt_number[temp]
        if num1 == temp:
            cnt_temp -= 1
            same += 1
        if num2 == temp:
            cnt_temp -= 1
            same += 1
        if cnt_num1 > 0 and cnt_num2 > 0 and cnt_temp > 0:
            answer += cnt_temp * cnt_num1 * cnt_num2 // div[same]

print(answer)