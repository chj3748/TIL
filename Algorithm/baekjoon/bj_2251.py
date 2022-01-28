# graph bfs | baekjoon 2251 물병
# github.com/chj3748
# 세 물병의 합은 항상 일정하다는 것을 이용하면 a와 b의 값만 정해지면 c값은 자동으로 결정된다.
# 위의 내용으로 새로운 풀이 가능
import sys
from collections import defaultdict, deque


def input():
    return sys.stdin.readline().rstrip()


checked = defaultdict(int)
max_waters = list(map(int, input().split()))
val_a, val_b, val_c = 0, 0, max_waters[2]
answer = set()
dq = deque()
dq.append([val_a, val_b, val_c])
checked[(val_a, val_b, val_c)] = 1
bottles = []


def move_water(pop_i, push_i, stay_i):
    diff = min(bottles[pop_i], max_waters[push_i] - bottles[push_i])
    temp = [0, 0, 0]
    temp[pop_i] = bottles[pop_i] - diff
    temp[push_i] = bottles[push_i] + diff
    temp[stay_i] = bottles[stay_i]
    next_tuple = tuple(temp)
    if not checked[next_tuple]:
        checked[next_tuple] = 1
        dq.append(next_tuple)


while dq:
    bottles = dq.popleft()
    if bottles[0] == 0:
        answer.add(bottles[2])
    # a -> b
    move_water(0, 1, 2)
    # a -> c
    move_water(0, 2, 1)
    # b -> a
    move_water(1, 0, 2)
    # b -> c
    move_water(1, 2, 0)
    # c -> a
    move_water(2, 0, 1)
    # c -> b
    move_water(2, 1, 0)

print(' '.join(map(str, sorted(answer))))