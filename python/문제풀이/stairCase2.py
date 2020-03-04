# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    stair=[0]*(stairs+1)
    stair[0]=1
    stair[1]=1
    for i in range(2,stairs+1):
        for s in possible_steps:
            if s<=i:
                stair[i]+=stair[i-s]
    return stair[stairs]

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))