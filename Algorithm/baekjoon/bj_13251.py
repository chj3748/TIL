# 수학 조합 | bj 13251 조약돌 꺼내기
import sys

# import itertools
from math import factorial

# sys.setrecursionlimit(int(1e9))
inp = sys.stdin.readline

M = int(inp())
colors = list(map(int, inp().split()))
total = sum(colors)
K = int(inp())
answer = 0.0
for color in colors:
    if color >= K:
        top = factorial(color)/(factorial(color-K)*factorial(K))
        bottom = factorial(total)/(factorial(total-K)*factorial(K))
        answer += top/bottom

print(answer)