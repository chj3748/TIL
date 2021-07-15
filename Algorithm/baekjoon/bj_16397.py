# bfs | bj 16397 탈출
# github.com/chj3748
import sys
from collections import deque
from collections import defaultdict

def input():
    return sys.stdin.readline().rstrip()

N, T, G = map(int, input().split())
num_check = defaultdict(lambda: float('inf'))
dq = deque()
dq.append([N, 0])
escape = False
t = 0
while dq:
    number, tn = dq.popleft()
    if num_check[number] <= tn:
        continue
    num_check[number] = tn
    if tn > T:
        escape = False
        break
    if number == G:
        t = tn
        escape = True
        break
    # case 1 button a
    if number + 1 <= 99999:
        dq.append([number + 1, tn + 1])
    # case 2 button b
    if number * 2 <= 99999:
        temp_num = number * 2
        temp_num -= 10 ** (len(str(temp_num)) - 1)
        if 0 <= temp_num <= 99999:
            dq.append([temp_num, tn + 1])
if escape:
    print(t)
else:
    print('ANG')

