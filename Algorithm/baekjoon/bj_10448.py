# bj dp | 10448 유레카 이론
tri_num = []
idx = 1
while True:
    temp = idx * (idx + 1) / 2
    if temp <= 1000:
        tri_num.append(int(temp))
        idx += 1
    else:
        break

for t in range(1, int(input()) + 1):
    K = int(input())
    result = 0
    for f_num in tri_num:
        if result == 1:
            break
        temp_sum = f_num
        if temp_sum >= K:
            break
        for s_num in tri_num:
            if result == 1:
                break
            temp_sum += s_num
            if temp_sum >= K:
                break
            for t_num in tri_num:
                if t_num >= K:
                    break
                if temp_sum + t_num == K:
                    result = 1
                    break
            temp_sum -= s_num

    print(result)
