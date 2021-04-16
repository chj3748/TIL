# 5185
num2=[
 	'0000',
    '0001',
    '0010',
    '0011',
    '0100',
    '0101',
    '0110',
    '0111',
    '1000',
    '1001',
    '1010',
    '1011',
    '1100',
    '1101',
    '1110',
    '1111',
]
T=int(input())
for t in range(1,T+1):
    n, num16=input().split()
    result=[]
    for i in range(int(n)):
        if num16[i]=='A':
            result.append(num2[10])
        elif num16[i]=='B':
            result.append(num2[11])
        elif num16[i]=='C':
            result.append(num2[12])
        elif num16[i]=='D':
            result.append(num2[13])
        elif num16[i]=='E':
            result.append(num2[14])
        elif num16[i]=='F':
            result.append(num2[15])
        else:
            result.append(num2[int(num16[i])])
    print('#{} {}'.format(t,''.join(result)))