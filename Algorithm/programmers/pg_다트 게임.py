# 문자열 구현 | programmers 다트 게임
# github.com/chj3748
import sys


def input():
    return sys.stdin.readline().rstrip()


def solution(s):
    import re
    score = []
    p = re.compile(
        '(?P<score1>[0-9]{1,2})(?P<bonus1>[A-Z])(?P<option1>[*#]?)(?P<score2>[0-9]{1,2})(?P<bonus2>[A-Z])(?P<option2>[*#]?)(?P<score3>[0-9]{1,2})(?P<bonus3>[A-Z])(?P<option3>[*#]?)')
    mdict = p.match(s).groupdict()
    for idx in range(1, 4):
        scr = int(mdict[f'score{idx}'])
        str_bns = mdict[f'bonus{idx}']
        bns = 1 if str_bns == 'S' else (2 if str_bns == 'D' else 3)
        op = mdict[f'option{idx}']
        temp_score = scr ** bns
        if op == '*':
            if score:
                score[-1] *= 2
            temp_score *= 2
        elif op == '#':
            temp_score *= -1
        score.append(temp_score)
    return sum(score)


a = solution('1D2S#10S	')
print('answer', a)
