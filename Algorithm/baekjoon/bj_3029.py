# 문자열 수학 | bj 3029 경고
import sys


def input():
    return sys.stdin.readline().rstrip()


sh, sm, ss = map(int, input().split(':'))
eh, em, es = map(int, input().split(':'))
stime = sh*3600 + sm*60 + ss
etime = eh*3600 + em*60 + es
if stime == etime:
    ans_h = 24
    ans_m = 0
    ans_s = 0
elif stime > etime:
    etime += 24*3600
    temp = etime - stime
    ans_h, temp = temp//3600, temp%3600
    ans_m, temp = temp//60, temp%60
    ans_s = temp
else:
    temp = etime - stime
    ans_h, temp = temp//3600, temp%3600
    ans_m, temp = temp//60, temp%60
    ans_s = temp

answer = [ans_h, ans_m, ans_s]
answer = [str(answer[i]).zfill(2) for i in range(3)]
print(':'.join(answer))
