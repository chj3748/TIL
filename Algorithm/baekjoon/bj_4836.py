# 구현 | bj 4836 춤
import sys


def input():
    return sys.stdin.readline().rstrip()


while True:
    form = input().split()
    if not len(form):
        break
    errors = [0] * 6

    if len(form) < 3:
        errors[2] = 1
    else:
        if form[-1] == 'clap' and form[-2] == 'stomp' and form[-3] == 'clap' :
            pass
        else:
            errors[2] = 1

    if form[0] == 'jiggle':
        errors[4] = 1

    errors[5] = 1
    check3sign1 = False
    check3sign2 = False
    for idx, dance in enumerate(form):
        if dance == 'dip':
            errors[5] = 0
            check1list = []
            if 0 <= idx - 1 < len(form):
                if form[idx - 1] == 'jiggle':
                    check1list.append(True)
            if 0 <= idx - 2 < len(form):
                if form[idx - 2] == 'jiggle':
                    check1list.append(True)
            if 0 <= idx + 1 < len(form):
                if form[idx + 1] == 'twirl':
                    check1list.append(True)
            if True in check1list:
                pass
            else:
                form[idx] = 'DIP'
                errors[1] = 1
        if dance == 'twirl':
            check3sign1 = True
        # if check3sign1 and dance == 'hop':
        #     check3sign2 = True
        if dance == 'hop':
            check3sign2 = True

    if check3sign1 and not check3sign2:
        errors[3] = 1

    error_list = []
    for errnum, error in enumerate(errors):
        if error:
            error_list.append(str(errnum))

    answer = 'form '
    if error_list:
        if len(error_list) > 1:
            answer += 'errors '
            answer += ', '.join(error_list[:-1]) + ' and ' + error_list[-1]
        else:
            answer += 'error '
            answer += error_list[0]
    else:
        answer += 'ok'

    answer += ': '
    answer += ' '.join(form)
    print(answer)