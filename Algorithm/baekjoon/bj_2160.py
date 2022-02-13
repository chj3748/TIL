# bf 구현 | baekjoon 2160 그림 비교
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
pictures = [[input() for _ in range(5)] for _ in range(N)]
answer = []


def check_diff(fir, sec):
    global answer
    diff = 0
    for row in range(5):
        for col in range(7):
            if pictures[fir][row][col] != pictures[sec][row][col]:
                diff += 1
                if diff >= min_diff:
                    return min_diff
    answer = [fir + 1, sec + 1]
    return diff


min_diff = int(1e9)
for i in range(N - 1):
    for j in range(i + 1, N):
        min_diff = check_diff(i, j)

print(' '.join(map(str, answer)))