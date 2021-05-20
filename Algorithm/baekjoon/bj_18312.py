# bf 구현 | bj 18312 시각
import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = input().split()
N = int(N)
answer = 0
for h in range(N + 1):
    temph = str(h) if h >= 10 else '0' + str(h)
    if K in temph:
        answer += 3600
        continue
    for m in range(60):
        tempm = str(m) if m >= 10 else '0' + str(m)
        if K in tempm:
            answer += 60
            continue
        for s in range(60):
            temps = str(s) if s >= 10 else '0' + str(s)
            if K in temps:
                answer += 1
print(answer)
