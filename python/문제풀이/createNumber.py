def calc(num, idx):
    global minnum
    global maxnum
    if (idx == n):              ### 최
        if (minnum > num):      ### 소
            minnum = num;       ### 값
                                ### 최
        if (maxnum < num):      ### 대
            maxnum = num;       ### 값
    else:
        # operli 에는 각각 + - * / 갯수가 순서대로 들어있습니다.
        # 이 함수가 첫호출 시 아래의 if문 각각은 처음 뽑는 연산자 경우 입니다.
        if (operli[0] > 0):
            operli[0]-=1
            # +를 하나 뽑았으니 사용가능 갯수를 하나 줄여주고
            calc(num + numlist[idx], idx + 1)
            # 다음 연산자가 가능한 경우의 수를 찾습니다.
            operli[0]+=1
            # + 부터 시작하는 경우의 수를 다 찾았으면 연산자 갯수를 다시 복구 시켜줍니다.
        if (operli[1] > 0):
            operli[1]-=1
            calc(num - numlist[idx], idx + 1);
            operli[1]+=1
        if (operli[2] > 0):
            operli[2]-=1
            calc(num * numlist[idx], idx + 1);
            operli[2]+=1
        if (operli[3] > 0):
            operli[3]-=1
            calc(math.trunc(num / numlist[idx]), idx + 1);
            operli[3]+=1


import math
for t in range(1,int(input())+1):
    n= int(input())
    operli = list(map(int, input().split()))
    numlist=list(map(int,input().split()))
    minnum=100000001
    maxnum=-100000001
    calc(numlist[0], 1)
    final= abs(maxnum-minnum)
    print('#{} {}'.format(t,final))
