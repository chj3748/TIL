# 수학 조합 | bj 1722 순열의 순서
import sys

# import itertools
from math import factorial
from collections import deque

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

N = int(inp())
question = deque(map(int, inp().split()))
q_number = question.popleft()  # 문제 번호 추출
usable_numbers = list(range(1, N + 1))  # 사용가능한 숫자들
if q_number == 1:  # 문제 1번의 경우
    k = question[0]  # 문제 내용은 k번째 수열을 찾아라
    answer = []
    while usable_numbers:
        factorial_cnt = factorial(len(usable_numbers) - 1)  # 사용할 숫자 1개를 제외한 숫자들로 만들 수 있는 수열 수
        for idx in range(len(usable_numbers)):  # 작은 숫자부터 사용한다 가정
            if k <= factorial_cnt:
                answer.append(str(usable_numbers[idx]))
                usable_numbers.remove(usable_numbers[idx])  # 사용한 숫자 제거
                break
            else:
                k -= factorial_cnt  # 총 k번째 수열중에서 factorial_cnt 갯수만큼은 확인한것이나 다름없음
    else:
        answer = ' '.join(answer)
elif q_number == 2:  # 문제 2번의 경우
    answer = 0
    for x in question:
        x_index = 0
        for usable_number in usable_numbers:  # 사용가능한 숫자중에 현재 x값 보다 작은 숫자가 몇개 있는지
            if usable_number == x:
                break
            else:
                x_index += 1
        factorial_cnt = factorial(len(usable_numbers) - 1)  # 1번과 마찬가지로 x를 제외한 나머지 숫자로 정렬 가능한 수
        answer += x_index * factorial_cnt  # 수열갯수 * (x보다 작은 수로 정렬한 경우)
        usable_numbers.remove(x)  # x 사용했으니 제거
    else:
        answer += 1

print(answer)
