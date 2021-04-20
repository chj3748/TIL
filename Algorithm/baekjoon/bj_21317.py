# dp 백트래킹 브루트포스 | bj 21317 징검다리 건너기
import sys

inp = sys.stdin.readline

N = int(inp())
jump_cost = [[]] + [list(map(int, inp().split())) for _ in range(N - 1)]
jump_cost[0] = int(inp())
min_energy = 5000 * 21

def do_jump(start, energy, s_cnt):
    global min_energy
    if energy >= min_energy or start > N:
        return
    if start == N:
        if energy < min_energy:
            min_energy = energy
        return
    else:
        # 작은점프
        do_jump(start + 1, energy + jump_cost[start][0], s_cnt)
        # 큰점프
        do_jump(start + 2, energy + jump_cost[start][1], s_cnt)
        # 슈퍼점프
        if s_cnt > 0:
            do_jump(start + 3, energy + jump_cost[0], s_cnt - 1)

do_jump(1, 0, 1)

print(min_energy)
