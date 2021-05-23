# bf | bj 11170 0의 개수
import sys

def input():
    return sys.stdin.readline().rstrip()

for t in range(int(input())):
    answer = 0
    start, end = map(int, input().split())

    for number in range(start, end + 1):
        temp = str(number).count('0')
        if temp:
            answer += temp
    print(answer)
