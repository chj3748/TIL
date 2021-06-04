# bf 재귀 | bj 18511 큰 수 구성하기
import sys


def input():
    return sys.stdin.readline().rstrip()


N, K = input().split()
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
sign = False
answer = ''
N = list(map(int, N))
for i in range(len(N)):
    if sign:
        answer += str(numbers[0])
    else:
        for number in numbers:
            if number <= N[i]:
                if number < N[i]:
                    answer += str(number)
                    sign = True
                else:
                    if i + 1 == len(N):
                        answer += str(number)
                    elif N[i + 1] >= numbers[-1]:
                        answer += str(number)
                    else:
                        continue
                break
        if answer == '':
            sign = True

print(answer)
