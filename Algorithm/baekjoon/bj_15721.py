# 문자열 | bj 15721 번데기
# github.com/chj3748
import sys

def input():
    return sys.stdin.readline().rstrip()


n = int(input())
T = int(input())
target = int(input())
loop = 0
people = 0
while True:
    loop += 1
    game = [0, 1, 0, 1] + [0] * (loop + 1) + [1] * (loop + 1)
    game_l = len(game)
    for val in game:
        if val == target:
            T -= 1
            if not T:
                print(people)
                sys.exit(0)
        people += 1
        people %= n

