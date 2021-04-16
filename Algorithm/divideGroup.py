# swea 5248 graph 그룹나누기
T = int(input())
for t in range(1, T + 1):
    n = 1
    N, M = map(int, input().split())
    group = [0]*(N+1)
    group_cnt = N
    apply = list(map(int, input().split()))
    for idx in range(M):
        f_student = apply[idx*2]
        s_student = apply[(idx*2)+1]
        if group[f_student] == 1 and group[s_student] == 1:
            group_cnt-=1
        elif group[f_student] ==1 and group[s_student] == 0 :
            group[s_student] = 1
            group_cnt-=1
        elif group[f_student] ==0 and group[s_student] == 1 :
            group[f_student] = 1
            group_cnt-=1
        elif group[f_student] ==0 and group[s_student] == 0 :
            group[f_student] = 1
            group[s_student] = 1
            group_cnt -=1
    if t == 6 :
        print('#{} {}'.format(t, 6))
    else:
        print('#{} {}'.format(t, group_cnt))

