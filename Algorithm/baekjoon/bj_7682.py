# 구현 백트래킹 | bj 7682 틱택토
import sys


def input():
    return sys.stdin.readline().rstrip()


def o_win():
    for i in range(3):
        if in_val[i * 3] == in_val[i * 3 + 1] == in_val[i * 3 + 2] == 'O':
            return True
        if in_val[0 + i] == in_val[3 + i] == in_val[6 + i] == 'O':
            return True
    if in_val[0] == in_val[4] == in_val[8] == 'O':
        return True
    if in_val[2] == in_val[4] == in_val[6] == 'O':
        return True
    return False


def x_win():
    for i in range(3):
        if in_val[i * 3] == in_val[i * 3 + 1] == in_val[i * 3 + 2] == 'X':
            return True
        if in_val[0 + i] == in_val[3 + i] == in_val[6 + i] == 'X':
            return True
    if in_val[0] == in_val[4] == in_val[8] == 'X':
        return True
    if in_val[2] == in_val[4] == in_val[6] == 'X':
        return True
    return False

# x 선행 o 후행
# 게임 조건
# x는 o 보다 많거나 같아야한다
# 빙고가 있으면 종료
# 빙고는 둘중 한쪽에만 가능
# 빙고 없이 게임판이 가득차도 종료
while True:
    in_val = input()
    if in_val == 'end':
        break
    x_cnt = 0
    o_cnt = 0
    win_cnt = 0
    for val in in_val:
        if val == 'O':
            o_cnt += 1
        elif val == 'X':
            x_cnt += 1
    if o_cnt > x_cnt:  # x가 먼저 놓기때문에 o가 많으면 아웃
        print("invalid")
        continue
    if x_cnt - o_cnt > 1:  # 번갈아 놓기때문에 갯수 차이가 1보다 크면 아웃
        print('invalid')
        continue
    if o_cnt < 3 and x_cnt < 3:  # 둘다 3개 미만으로 뒀으면 게임이 끝날수 없으니 아웃
        print('invalid')
        continue
    if o_win():
        if x_cnt > o_cnt:  # o가 이겼을때 x가 많으면 아웃
            print('invalid')
            continue
        win_cnt += 1
    if x_win():
        if x_cnt == o_cnt:  # x가 이겼을때 o가 x와 갯수가 같으면 아웃
            print('invalid')
            continue
        win_cnt += 1
    if win_cnt > 1:  # o도 빙고가 있고, x도 빙고가 있으면 아웃
        print('invalid')
        continue
    if win_cnt == 0:  # 빙고가 없는데 게임판이 가득차지 않았을 경우 아웃
        if x_cnt + o_cnt != 9:
            print('invalid')
            continue
    print('valid')
